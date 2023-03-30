function [robot] = initialization()

    % Initialize robot
    robot = JacoComm;
    connect(robot);

    % Initialize fingers to default ('open')
    calibrateFingers(robot);
    sendFingerPositionCommand(robot,[0;0;0]);

    % Initialize position to default ('home')
    setPositionControlMode(robot);
    goToHomePosition(robot);
    disp(robot.EndEffectorPose);

end
