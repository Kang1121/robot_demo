"""
Some tested values for individual joint movement only (exceeding value assignment may cause danger)
Joint 1 --> no limit
Joint 2 --> 1.0 ~ 4.2
Joint 3 --> no limit
Joint 4 --> 0.5 ~ 5.5
Joint 5 --> no limit
Joint 6 --> 1.2 ~ 5.2
Joint 7 --> no limit
"""

from __future__ import division, print_function, absolute_import, unicode_literals
import time
import numpy as np
from utils import *
from collections import OrderedDict


if __name__ == "__main__":

    # Initialize Robotic Arm API and move to Home to stand by
    robotic_arm = api_init()
    # des_pos = np.round(np.array(get_angular_pos(robotic_arm)))
    # print(des_pos)

    # move(robotic_arm, py2mat([[283.23], [162.70], [0], [43.59], [265.23], [257.52], [288.14]]), 0)
    # move(robotic_arm, py2mat([[0], [0], [0]]), 0)

    # # Move arm to home position
    # start = time.time()
    # print('Time elapsed for initialization: ', time.time() - start)

    # print('\nTell me what to do: "home", "end"...')
    # user_input = input()

    # while user_input != 'end':
    #     if user_input == 'automation':
    #         pos = get_pos('preset')
    #         pos = OrderedDict(reversed(list(pos.items())))
    #
    #         while bool(pos):
    #             cmd = pos.popitem()[1]
    #             interval = cmd.pop()
    #             move(robotic_arm, py2mat(cmd), interval)
    #
    #     else:
    #         pos = get_pos('positions')
    #         if user_input == 'home':
    #             move(robotic_arm, py2mat(pos['home']), 0)
    #         else:
    #             pass
    #     # Destination position
    #     # des_pos = get_angular_pos(robotic_arm)
    #     # print(des_pos)
    #     # Get new position inputs
    #     print('\n I am moving... In the meantime, you can tell me what to do next!:')
    #     user_input = input()

    # End of program
    # print('Bye!')

    pos = OrderedDict(reversed(list(get_pos('preset').items())))

    while bool(pos):
        name, cmd = pos.popitem()
        print(name)
        print('-' * 30)
        sleep, interval = cmd.pop(), cmd.pop()
        move(robotic_arm, py2mat(cmd), interval, sleep)

    robotic_arm[0].quit()
