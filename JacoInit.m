function [jc, pos, vel, torque, temp, effector_pos] = JacoInit(finger_pos)
% Jaco initialization
jc = JacoComm;
connect(jc);
calibrateFingers(jc);

%% Query individual object properties, robotic arm initialization
jc.JointPos
%%
jc.JointVel
%%
jc.JointTorque
%%
jc.JointTemp
%%
jc.FingerPos
%%
jc.FingerVel
%%
jc.FingerTorque
%%
jc.FingerTemp
%%
jc.EndEffectorPose
%%
jc.EndEffectorWrench
%%
jc.ProtectionZone
%%
jc.EndEffectorOffset
%%
jc.DOF
%%
jc.TrajectoryInfo

%% Methods to query joint and finger values all at once
%% �� ���� ���� ���� �հ��� ���� ���� ���� ����
pos = getJointAndFingerPos(jc);
%%
%% �� ���� �ӵ� ���� �հ��� ���� �ӵ� ���� ����
vel = getJointAndFingerVel(jc);
%%
%% �� ���� ��ũ ���� �հ��� ���� ��ũ ���� ����
torque = getJointAndFingerTorque(jc);
temp = getJointAndFingerTemp(jc);

setPositionControlMode(jc);
goToHomePosition(jc);

effector_pos=jc.EndEffectorPose;

setPositionControlMode(jc);

sendFingerPositionCommand(jc,finger_pos);
end

