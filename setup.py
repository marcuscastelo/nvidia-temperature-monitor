import generate_systemd_units
import os
import configparser

config = configparser.ConfigParser()
config.read('settings.cfg')

SYSTEMD_PATH = config['SYSTEMD']['SYSTEMD_PATH']
SERVICE_BASENAME = config['SYSTEMD']['SERVICE_BASENAME']

def install_units():
	os.system('cp ./systemd-units/* %s' % SYSTEMD_PATH)

def enable_units():
	os.system('systemctl enable --now %s-timered.service' % SERVICE_BASENAME)
	os.system('systemctl enable --now %s-timered.timer' % SERVICE_BASENAME)
	os.system('systemctl enable --now %s-boothook.service' % SERVICE_BASENAME)

def setup():
	print('Assure the script is running with root privileges')
	print("Creating systemd services...")
	generate_systemd_units.generate_units()

	print('Installing services...')
	install_units()
	print('Success!')
	choice = input('Would you like to enable installed services? [Y/n] ')
	if choice != 'n' and choice != 'N':
		enable_units()


if __name__ == '__main__':
	setup()
else:
	print('setup.py should not be imported as a module')