import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import ActuatorCommand


class ActuatorCommandPublisher(Node):
    def __init__(self):
        super().__init__('actuator_command_publisher')

        # 파라미터 선언 (기본값 1500, 범위 1000~2000)
        self.declare_parameter('motor_pwm', 1500.0)
        self.declare_parameter('steering_pwm', 1500.0)

        # PX4 QoS 설정
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.publisher_ = self.create_publisher(
            ActuatorCommand,
            '/fmu/in/actuator_command',
            qos_profile
        )

        # 파라미터 실시간 변경 콜백 등록
        self.add_on_set_parameters_callback(self.parameter_callback)

        self.timer = self.create_timer(0.1, self.publish_command)  # 10Hz
        self.get_logger().info('ActuatorCommand Publisher 시작 (motor_pwm=1500, steering_pwm=1500)')

    def clamp_pwm(self, value: float) -> float:
        """PWM 값을 1000~2000 사이로 제한"""
        return max(1000.0, min(2000.0, value))

    def parameter_callback(self, params):
        """파라미터가 변경될 때 호출되는 콜백"""
        from rcl_interfaces.msg import SetParametersResult

        for param in params:
            if param.name == 'motor_pwm':
                clamped = self.clamp_pwm(param.value)
                self.get_logger().info(f'[파라미터 변경] motor_pwm: {param.value} → 적용값: {clamped}')
            elif param.name == 'steering_pwm':
                clamped = self.clamp_pwm(param.value)
                self.get_logger().info(f'[파라미터 변경] steering_pwm: {param.value} → 적용값: {clamped}')

        return SetParametersResult(successful=True)

    def publish_command(self):
        # 현재 파라미터 값 읽기
        motor_pwm   = self.clamp_pwm(self.get_parameter('motor_pwm').value)
        steering_pwm = self.clamp_pwm(self.get_parameter('steering_pwm').value)

        msg = ActuatorCommand()
        msg.timestamp    = self.get_clock().now().nanoseconds // 1000  # microseconds
        msg.motor_pwm    = motor_pwm
        msg.steering_pwm = steering_pwm

        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Published → motor_pwm: {msg.motor_pwm:.1f}, steering_pwm: {msg.steering_pwm:.1f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ActuatorCommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()