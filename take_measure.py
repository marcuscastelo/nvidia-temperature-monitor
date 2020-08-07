#!/bin/python

import subprocess
import configparser
import os
from datetime import datetime

config = configparser.ConfigParser()
config.read('settings.cfg')

if 'MEASURES' not in config or 'DATA_FOLDER' not in config['MEASURES']:
	print("Bad settings.cfg, see settings_model.cfg")
	exit(1)

# Command to measure temperature in linux using nvidia proprietary drivers
MEASURE_COMMAND = "nvidia-smi -i 0 -q -d TEMPERATURE | grep 'GPU Current' | awk -F ':' '{print $2}' | awk -F ' ' '{print $1}'"

process = subprocess.Popen(MEASURE_COMMAND, shell=True, stdout=subprocess.PIPE)
(out, err) = process.communicate()
process.wait()

curr_temperature = out.decode('utf-8')[:-1:]
data_folder = config['MEASURES']['DATA_FOLDER']
curr_date = datetime.today().strftime('%Y-%m-%d')
curr_time = datetime.today().strftime('%H:%M:%S')

filename = 'temperatures-%s' % curr_date
file_path = '%s/%s' % (data_folder, filename)

with open(file_path, 'a+') as f:
	f.write('%s -> \t%s\n' % (curr_time, curr_temperature))