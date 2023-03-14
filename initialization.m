function [jc] = initialization()

    jc = JacoComm;
    connect(jc);
    calibrateFingers(jc);
    setPositionControlMode(jc);

end

