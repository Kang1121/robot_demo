function [current_pos] = control(robot,task,param,lag,varargin)

    % Get current position of end effectors
    current_pos = robot.EndEffectorPose;
    disp(current_pos);
    disp(param);
    
    % Perform the specified task
    switch (task)
        case 'reach'
            % Check workspace limits (limit_x = 0.9, limit_y = 0.9, limit_z = 1.1)
            if any(abs(param(1:3)) > [0.9; 0.9; 1.1]) || (param(3) < 0)
                disp('Out of bounds!');
                return
            end
            param = param(1:3) - current_pos(1:3); disp(param);
            command = [param(:); 0; 0; 0]; 
            sendCartesianPositionCommand(robot, command);
            pause(lag);

        case 'adjust'
            pitch = 0;
            if pi/2-current_pos(5) > 0.01, pitch=pi/2-current_pos(5); end
            command = [param(:); 0; pitch; 0];
            sendCartesianPositionCommand(robot, command);
            pause(lag);

        case 'grasp'
            command = param*ones(3,1);
            sendFingerPositionCommand(robot,command);
            pause(lag);

        case 'twist'
            command = [0; 0; 0; 0; 0; 0; deg2rad(param)]; disp(command);
            for i=1:varargin{1}
                sendJointVelocityCommand(robot,command);
            end
            pause(lag);
    end

    current_pos = robot.EndEffectorPose;
    disp(current_pos);

end
