import math
import matlab
import matlab.engine
import yaml
from yaml.loader import SafeLoader

class RobotControlModule:
    def __init__(self, preset, verbose=False):
        self.controller = self.api_init()
        self.arm = self.controller.initialization(nargout=1)
        self.world = self.get_params(preset)
        self.verbose = verbose
        # TODO: self.joints = ... current state of joints

    def api_init(self):

        # Create a matlab session named "controller"
        controller = matlab.engine.start_matlab()
        matlab_api_path = controller.genpath('matlab_api')

        # Add necessary matlab functions into the path
        controller.addpath(matlab_api_path, nargout=0)

        return controller

    @staticmethod
    def get_params(preset):

        # Open the file and load the file
        with open(f'{preset}.yaml') as f:
            params = yaml.load(f, Loader=SafeLoader)

        return params

    def reach_to(self, obj, lag=0):
        """
        Reach to an object using pre-defined joint commands
        object: high-level reach command (name of object to reach to, pre-defined in preset.yaml)
        lag: length of pause after the movement (in seconds)
        """
        if obj in self.world.keys():
            params = self.world[obj]
        else:
            raise ValueError(f'Unrecognized object: {obj}')

        # Create a nested list of params to feed to matlab function
        params = matlab.double([[math.radians(i)] for i in params])

        if self.verbose:
            print(f'Moving to {obj}')
            print('-' * 30)

        # Execute command and update current state of joints
        self.controller.control(self.arm, 'reach', params, 0, lag, nargout=0)
        # TODO: self.joints = params

    def twist(self, cmd='right', angle=180, lag=0):
        """
        Twist the wrist (7th joint) using pre-defined param
        cmd: high-level twist command. choices=['left', 'right']
        angle: twist-related param (can be taken as twisting angle)
        lag: length of pause after the movement (in seconds)
        """
        if cmd == 'right':
            wrist = -30
        elif cmd == 'left':
            wrist = 30
        else:
            raise ValueError(f'Unrecognized twist command: {cmd}')

        # Create a nested list of params to feed to matlab function
        params = [0]*6 + [wrist]  # set 6 other joints to 0
        params = matlab.double([[math.radians(i)] for i in params])

        # Execute command and update current state of joints
        self.controller.control(self.arm, 'twist', params, angle, lag, nargout=0)
        # TODO: self.joints = params

    def grasp(self, cmd='open', lag=0):
        """
        Move the 3 fingers using pre-defined param
        cmd: high-level grasp command. choices=['open', 'close']
        lag: length of pause after the movement (in seconds)
        """
        if cmd == 'close':
            finger = 4000
        elif cmd == 'open':
            finger = 0
        else:
            raise ValueError(f'Unrecognized grasp command: {cmd}')

        # Create a nested list of params to feed to matlab function
        params = [[finger]]*3  # 3 fingers total
        params = matlab.double(params)

        # Execute command and update current state of joints
        self.controller.control(self.arm, 'grasp', params, 0, lag, nargout=0)
        # TODO: self.joints = params

    def rest(self):
        if self.verbose:
            print(f'Bye!')
        self.controller.quit()
