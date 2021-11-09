from subprocess import check_call

backend_folder = '/srv/beefgs02/scratch/aegis_guardian/data/NEW_BACKEND/'

# get with api from muftawo
integer_key = 133947
ride_id = 'Ride001'


def extraction():
    check_call(['./extract.sh', str(integer_key),ride_id])


extraction()