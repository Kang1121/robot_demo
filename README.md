# robot_demo

This Python code for robotic arm control is a wrapper of official MATLAB codes.

## Prerequisites
> * Windows System
> * MATLAB 2021b
> * Anaconda
```
conda create -n demo python=3.7
conda activate demo
pip install matlabengine==9.11.19
```
Download [official SDK](https://drive.google.com/file/d/1UEQAow0XLcVcPCeQfHK9ERBihOCclkJ9/view) and install
> * Kinova-Jaco-Usb-Driver-(usblib)-Installer
> * SDK_GEN2_1_5_1_x86
## Run
We design a simple but complete scenario of drinking water. 
To run, first make sure the robotic arm is corrected connected and be recognized by computer, then open Anaconda Powershell Prompt and enter:
```
git clone git@github.com:Kang1121/robot_demo.git
cd robot_demo
python main.py
```
## Customize you scenario
Please make sure you have no running connections (e.g. connected IDEs or terminals) to the robotic arm before you do the following operations.
> * Open the installed SDK 'Development Center', wait until the device ID is recognized and shown on the top right corner.
> * Control the arm with 'Virtual Joystick'.
> * Get current cartesian/joint values with 'Trajectory Planner'.
## Common issues
> * It's not suggested to open Kinova Development Center while running our codes, which may cause connection failure to hardware. 
> * Simply restart terminal and reboot the robotic arm will fix most running errors.
