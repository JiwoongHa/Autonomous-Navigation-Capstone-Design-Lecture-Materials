close all; clc; clear;

addpath(genpath("D:\Jiung\matlab\대학원\2026-1학기\자율운항캡스톤디자인\tools"));

% Chungnam Univ. Building E5-1
ref_lat = 36.365227;
ref_lon = 127.345838;

% ref_lla = [36.365227, 127.401794, 25.1110]; % CNU
rel_lla = [36.364864, 127.344258, 25.1110 ]; % CNU 남부운동장
% ref_lla = [36.395991, 127.401794, 25.1110]; % SHI Square 33

[x_ref,y_ref,~] = deg2utm(ref_lat,ref_lon);

% RC min-max values
RC_max = 2000;
RC_min = 1000;

Fx_max = 1;
Fx_min = -1;

N_max = 1;
N_min = -1;