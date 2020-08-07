# Nvidia Temperature Monitor

## Description

A simple python script that creates a history of GPU temperatures measured with `nvidia-smi`. The measures are taken once at system startup and once before it shutdowns. There is also a configurable timer, which takes temperature measurements from time to time. All those features rely on **systemd units**

## Prerequisites

* Python 3 (Tested with 3.8.5)
* Systemd (If you are using other manager, the script will not work)
* nvidia-smi (The script is intended to be used with nvidia cards running on proprietary drivers)

## Installation

The first step is to clone this repository. Do it in a good place, since the installed systemd's unit is going to be pointing to that location after installed

After installing the prerequisites and cloning the repository, there is just one more step to take: \
Go to the clonned folder and execute the following command \
```console
user:nvidia-temperature-monitor$ sudo python ./setup.py

or

user:nvidia-temperature-monitor$ sudo python3 ./setup.py
```
The installer will prompt a user name and a group name, this is going to be used to set systemd unit's privileges, you might inform your user or other user.

## Configuration

You may mess with some configurations, such as how much time should be between measurements (in seconds), which name should the units have, etc...

![demonstration_of_settings.cfg](https://i.imgur.com/ABA1mET.png)
