# Homework-2

## Setup and Installation
[Colab notebook](https://colab.research.google.com/drive/1PmagnEr-OOMuIzNr25csAumyJ3Z6UpLQ?authuser=4)
[Course Website including writeup](https://courses.cs.washington.edu/courses/cse579/24au/projects/homework2/)
### Install MuJoCo

1. Download the MuJoCo version 2.1 binaries for
   [Linux](https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz) or
   [OSX](https://mujoco.org/download/mujoco210-macos-x86_64.tar.gz).
2. Extract the downloaded `mujoco210` directory into `~/.mujoco/mujoco210`.
3. Add resources/mjkey.txt in the repo into into `~/.mujoco/mujoco210`.

### Setup environment

To set up the project environment, Use the `environment.yml` file. It contains the necessary dependencies and installation instructions. It is the same as last assignment

    conda env create -f environment.yml
    conda activate cse579a1

### Install LibGLEW

    sudo apt-get install libglew-dev
    sudo apt-get install patchelf
    
### Export paths variables

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/.mujoco/mujoco210/bin
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
    
### Compile mujoco_py (only needs to be done once)
    python -c "import mujoco_py"
## What you have to do:
Follow the instructions in the write up to complete the TODOs in the following files:
- `policy_gradient.py`
- `actor_critic.py`
- `sac.py`
Psudeo code for each of these steps is provided in the write up at the end. Try to not use the pseudocode 
but it is there as a resource if you need it.
## Training
    python main.py  --task pg --env pendulum
    python main.py  --task actor_critic --env pendulum
    python main.py  --task sac --env pendulum
       
    

## Evaluation
    python main.py  --task pg --env pendulum --test
    python main.py  --task actor_critic --test --env pendulum
    python main.py  --task sac --test --env pendulum
    

