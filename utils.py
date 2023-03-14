import math
import matlab
import matlab.engine
import yaml
from yaml.loader import SafeLoader


def py2mat(pos):

    """10 elements in the pos, actuator 1-7, finger 1-3"""
    if len(pos) == 7:
        return matlab.double([[math.radians(i[0])] for i in pos])
    elif len(pos) == 3:
        return matlab.double([[i[0]] for i in pos])
    # elif len(pos) == 10:
    #     return matlab.double([[math.radians(i[0])] if i < 7 else [i[0]] for idx, i in enumerate(pos)])
    else:
        raise IndexError('Check the number of input dimensions')


def api_init():

    # Create a matlab session named "controller"
    matlab_session = matlab.engine.start_matlab()
    matlab_api_path = matlab_session.genpath('matlab_api')

    # Add necessary matlab functions into the path
    matlab_session.addpath(matlab_api_path, nargout=0)

    # Initialize Arm
    arm = matlab_session.initialization(nargout=1)

    return (matlab_session, arm)


def move(robotic_arm, des, interval, sleep):
    """
    Move to new position
    des: destination position in radian
    interval: twist related value (the last joint), can be taken as twisting angles
    sleep: sleep-time after the movement (in second)
    """
    (session, arm) = robotic_arm
    session.move(arm, des, interval, sleep, nargout=0)


def get_pos(file):

    # Open the file and load the file
    with open('{}.yaml'.format(file)) as f:
        pos = yaml.load(f, Loader=SafeLoader)

    return pos


if __name__ == "__main__":

    pass
