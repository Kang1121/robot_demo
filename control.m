function control(obj,type,cmd,angle,lag)
    switch (type)
        case 'reach'
            sendJointPositionCommand(obj,cmd);
            pause(lag);
            
        case 'grasp'
            sendFingerPositionCommand(obj,cmd);
            pause(lag);
            
        case 'twist'
            for i=1:angle
                sendJointVelocityCommand(obj,cmd);
            end
            pause(lag);
    end
end

