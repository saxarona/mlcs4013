% SVM
% A01170065 Xavier Sánchez
% A00806415 Gabriel González

% Clean everything
clear all;
close all;
clc

% Load dataset
[y, x] = libsvmread('Full.txt');

% parameters:
% C: cost, penalization for misclassified data
% gamma: usually 1/number_of_attrs.
% however, cross-validation gives the following:

gamma = 0.00048828125;
C = 8192;

% Training the model using the following:
% -s 0: which is SVM Classification (C-SVM)
% -t 2: kernel radial basis function, i.e. exp(-gamma*|u-v|^2)
% -c C: cost parameter of C-SVM

model = svmtrain(y, x, sprintf('-s 0 -t 2 -g %g -c %g -m 300', gamma, C));

w = model.SVs' * model.sv_coef;
b = -model.rho;

if (model.Label(1) == -1)
  w =  -w;
  b = -b;
endif

% load testing features and labels
[test_y, test_x] = libsvmread('Full_test.txt');

[predicted_label, accuracy, decision_values] = svmpredict(test_y, test_x, model);