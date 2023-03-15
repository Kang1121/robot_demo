"""
This program executes the following robotic arm control scenario:
- Reach and grasp water bottle -> Pour water into cup -> Bring cup to user

To change the scenario, modify the following in this code snippet:
- order and type of actions (reach, grasp, twist)
- length of pauses in-between actions ('lag' is in seconds)
- angle of twist ('angle' is in degrees. modify with care.)

To change or add objects, modify the config (yaml) file and this code accordingly.
"""
import argparse
from module import RobotControlModule


def run_scenario(robot):
    # Get ready
    robot.reach_to(obj='Home1', lag=10)
    robot.grasp(cmd='open', lag=3)
    robot.reach_to(obj='Standby1', lag=4)

    # Reach to bottle and grasp
    robot.reach_to(obj='Bottle1', lag=4)
    robot.grasp(cmd='close', lag=3)

    # Reach close to cup and pour water
    robot.reach_to(obj='Cup1', lag=2)
    robot.twist(cmd='left', angle=300, lag=6)
    robot.twist(cmd='right', angle=280, lag=3)

    # Put down bottle
    robot.reach_to(obj='Bottle2', lag=4)
    robot.grasp(cmd='open', lag=2)
    robot.reach_to(obj='Standby2', lag=4)

    # Reach to cup and grasp
    # requires micro-movement steps to avoid knocking off object (cup2, cup3, etc.)
    robot.reach_to(obj='Cup2')
    robot.reach_to(obj='Cup3')
    robot.reach_to(obj='Cup4', lag=3)
    robot.grasp(cmd='close', lag=3)

    # Bring cup to user and tilt cup
    robot.reach_to(obj='User', lag=3)
    robot.twist(cmd='left', angle=180, lag=6)
    robot.twist(cmd='right', angle=160, lag=3)

    # Put down cup
    robot.reach_to(obj='Cup5', lag=3)
    robot.grasp(cmd='open', lag=3)

    # Return to home position
    robot.reach_to(obj='Standby3')
    robot.reach_to(obj='Standby4')
    robot.reach_to(obj='Standby5', lag=3)
    robot.reach_to(obj='Home2', lag=4)
    robot.grasp(cmd='close')

    robot.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Robotic Arm Control')
    parser.add_argument('--preset', type=str, default='preset', help='name of preset config file')
    parser.add_argument('--verbose', action='store_true', help='robot likes to talk')
    args = parser.parse_args()

    # INITIALIZATION
    robotic_arm = RobotControlModule(preset=args.preset, verbose=args.verbose)

    # EXECUTION
    run_scenario(robotic_arm)
