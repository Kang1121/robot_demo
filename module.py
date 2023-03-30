import matlab
import matlab.engine
import yaml
from yaml.loader import SafeLoader
from typing import List


class RobotControlModule:
    def __init__(self, args):
        self.controller = self.api_init(args.api)
        self.arm = self.controller.initialization(nargout=1)
        self.world = self.get_preset(args.preset)
        self.verbose = args.verbose
        self.current_pos = 0

    @staticmethod
    def api_init(api_path):
        # Create a matlab session named "controller"
        controller = matlab.engine.start_matlab()
        matlab_api_path = controller.genpath(api_path)

        # Add necessary matlab functions into the path
        controller.addpath(matlab_api_path, nargout=0)

        return controller

    @staticmethod
    def get_preset(preset_path):
        # Open the file and load the file
        with open(f'{preset_path}.yaml') as f:
            preset = yaml.load(f, Loader=SafeLoader)

        return preset

    def reach(self, cmd: List[float] = None, lag=0): #, speed=0.1, delta=False):
        """
        Reach to a position given cartesian coordinates
        cmd: xyz cartesian coordinates of desired position
        lag: length of pause after the movement (in seconds)
        delta: whether the cmd is a delta value or not
        """
        # Create a nested list of commands to feed to matlab function
        if self.verbose:
            print(f'Reaching to {cmd}')
            print('-' * 30)
        cmd = matlab.double([[c] for c in cmd])

        # Execute command and update current state of joints
        current_pos = self.controller.control(self.arm, 'reach', cmd, lag, nargout=1)
        self.current_pos = current_pos

    def adjust(self, cmd: List[float] = None, lag=0):
        cmd = matlab.double([[c] for c in cmd])
        current_pos = self.controller.control(self.arm, 'adjust', cmd, lag, nargout=1)
        self.current_pos = current_pos

    def twist(self, cmd: str = 'right', lag=0, angle=180):
        """
        Twist the wrist (7th joint) using pre-defined param
        cmd: high-level twist command. choices=['left', 'right']
        angle: twist-related param (can be taken as twisting angle)
        lag: length of pause after the movement (in seconds)
        """
        if cmd == 'right':
            wrist = -30  # velocity of wrist joint
        elif cmd == 'left':
            wrist = 30
        else:
            raise ValueError(f'Unrecognized twist command: {cmd}')
        param = matlab.double([wrist])

        # Execute command and update current state of joints
        current_pos = self.controller.control(self.arm, 'twist', param, lag, angle, nargout=1)
        self.current_pos = current_pos

    def grasp(self, cmd: str = 'open', lag=0):
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
        param = matlab.double([finger])

        # Execute command and update current state of joints
        current_pos = self.controller.control(self.arm, 'grasp', param, lag, nargout=1)
        self.current_pos = current_pos

    def rest(self):
        if self.verbose:
            print(f'Bye!')
        self.controller.quit()
