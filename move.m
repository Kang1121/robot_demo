function [] = move(jc, jntCmd, interval, sleep)

    %switch (type)
    %    case 'joint'
    %        sendJointPositionCommand(jc, jntCmd);
    %    case 'finger'
    %        sendFingerPositionCommand(jc,jntCmd);
    %    case 'twist'
    %        for i=1:interval
    %            sendJointVelocityCommand(jc,jntCmd);
    %        end

    if length(jntCmd) == 7 && interval == 0
        sendJointPositionCommand(jc, jntCmd);
        pause(sleep);
    elseif length(jntCmd) == 7 && interval ~= 0
        for i=1:interval
            sendJointVelocityCommand(jc,jntCmd);
        end
        pause(sleep);
    elseif length(jntCmd) == 3 && interval == 0
        sendFingerPositionCommand(jc,jntCmd);
        pause(sleep);
    end

end
