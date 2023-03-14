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
## Run
We design a simple but complete scenario of drinking water. 
To run in the terminal, open Anaconda Prompt and enter:
```
git clone git@github.com:Kang1121/robot_demo.git
cd robot_demo
python main.py
```
## Common Issues
> * It's not suggested to open Kinova Development Center while running our codes, which may cause connection failure to hardware. 
> * Simply restart terminal and reboot the robotic arm will fix most running errors.
