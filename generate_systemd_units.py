import configparser
import os

config = configparser.ConfigParser()
config.read('settings.cfg')

DESCRIPTION = config['SYSTEMD']['DESCRIPTION']
SERVICE_BASENAME = config['SYSTEMD']['SERVICE_BASENAME']
TIMER_INTERVAL = config['SYSTEMD']['TIMER_INTERVAL']
TAKE_MEASURE_FILE_NAME = 'take_measure.py'

def generate_units():
	current_directory = os.getcwd()
	current_user = input('The service should be executed from which user? ')
	current_group = input('The service should be executed from which group? ')

	take_measure_script_path = '%s/%s' % (current_directory, TAKE_MEASURE_FILE_NAME)

	timer_str = '''[Unit]
Description=%s
Requires=%s-timered.service

[Timer]
OnActiveSec=%s
OnUnitInactiveSec=%s

[Install]
WantedBy=timers.target''' % (DESCRIPTION, SERVICE_BASENAME, TIMER_INTERVAL, TIMER_INTERVAL)

	timered_service_str = '''[Unit]
Description=%s

[Service]
WorkingDirectory=%s
ExecStart=%s
Type=oneshot
User=%s
Group=%s

[Install]
WantedBy=default.target''' % (DESCRIPTION, current_directory, take_measure_script_path, current_user, current_group)

	boothook_service_str = '''[Unit]
Description=%s

[Service]
WorkingDirectory=%s
ExecStart=%s
RemainAfterExit=true
ExecStop=%s
Type=oneshot
User=%s
Group=%s

[Install]
WantedBy=default.target''' % (DESCRIPTION, current_directory, take_measure_script_path, take_measure_script_path, current_user, current_group)

	os.system('mkdir systemd-units 2>/dev/null')
	with open('./systemd-units/%s-timered.timer' % SERVICE_BASENAME, 'w') as f:
		f.write(timer_str)
	with open('./systemd-units/%s-timered.service' % SERVICE_BASENAME, 'w') as f:
		f.write(timered_service_str)
	with open('./systemd-units/%s-boothook.service' % SERVICE_BASENAME, 'w') as f:
		f.write(boothook_service_str)

	print("Services created at %s/systemd-units" % current_directory)

if __name__ == '__main__':
	generate_units()