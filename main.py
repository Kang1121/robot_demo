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
from module_ex import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Robotic Arm Control')
    parser.add_argument('--preset', type=str, default='preset_ex', help='name of preset config file')
    parser.add_argument('--api', type=str, default='matlab_api', help='name of matlab api directory')
    parser.add_argument('--verbose', action='store_true', help='robot likes to talk')
    args = parser.parse_args()

    # INITIALIZATION
    robot = RobotControlModule(args)

    xyz = {'standby': [-0.09, -0.5, 0.07], 'user': [], } #, 'bottle': [], 'cup': []}
    robot.reach(cmd=xyz['standby'], lag=4)
    robot.twist(cmd='left', angle=180, lag=6)

    # EXECUTION
    # 1. Select object based on EEG classification result
    # TODO: cls = 'bottle' -> input to AR module

    # 2. Move close to object (bottle) using AR coordinates
    xyz['bottle'] = [0.15, -0.45, 0.1] # output of AR module
    robot.reach(cmd=xyz['bottle'], lag=4)

    # 3. Adjust based on EEG classification result
    cls = 'left'  # output of EEG module
    x = -0.05 if cls == 'right' else 0.05
    robot.adjust(cmd=[x, 0, 0], lag=4)

    # 4. Grasp object based on EEG classification result
    # Assume output was 'grasp' (true)
    robot.grasp(cmd='close', lag=3)

    # 5. Move close to object (cup) using AR coordinates
    xyz['cup'] = [0.35, -0.35, 0.1]
    pour_pos = xyz['cup'] + [0, 0, 0.1]
    robot.reach(cmd=pour_pos, lag=2)

    # 6. Adjust based on EEG classification result
    cls = 'right'
    x = -0.05 if cls == 'right' else 0.05
    robot.adjust(cmd=[x, 0, 0], lag=4)

    # 7. Twist object (bottle) based on EEG classification result
    # Assume output was 'twist' (true)
    robot.twist(cmd='left', angle=300, lag=6)
    robot.twist(cmd='right', angle=280, lag=3)

    # 8. Put object (bottle) back in original position
    robot.reach(cmd=xyz['bottle'], lag=4)
    robot.grasp(cmd='open', lag=3)

    # 9. Move close to object (cup) using AR coordinates
    robot.reach(cmd=xyz['cup'], lag=2)

    # 10. Adjust based on EEG classification result
    cls = 'right'
    x = -0.05 if cls == 'right' else 0.05
    robot.adjust(cmd=[x, 0, 0], lag=4, delta=True)

    # 11. Grasp object (cup) based on EEG classification result
    # Assume output was 'grasp' (true)
    robot.grasp(cmd='close', lag=3)

    # 12. Bring cup to user and tilt cup
    robot.reach(cmd=xyz['user'], lag=3)
    robot.twist(cmd='left', angle=180, lag=6)
    robot.twist(cmd='right', angle=160, lag=3)

    # 13. Put object (cup) back in original position
    robot.reach(cmd=xyz['cup'], lag=2)
    robot.grasp(cmd='open', lag=3)

    # 14. Return to home position
    robot.rest()
