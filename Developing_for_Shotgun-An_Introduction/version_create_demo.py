import shotgun_api3

SITE_URL = ''
SCRIPT_NAME = ''
SCRIPT_KEY = ''

# Create a connection to Shotgun
sg = shotgun_api3.Shotgun(SITE_URL, SCRIPT_NAME, SCRIPT_KEY)

# Find the project we'll be attaching our version to / simple filter
project = sg.find_one('Project', [['name', 'is', 'Hyperspace Madness']], ['id'])

# Find the shot we'll be attaching our version to / compound AND filter
shot = sg.find_one('Shot', [['code', 'is', 'SATL_0200'], ['project', 'is', project]], ['id'])

# Create our version attached to the project
version = sg.create('Version', {'project':project, 'entity':shot, 'code':'checkerboard.mov'})

# Update the version to link it to the shot
sg.update('Version', version['id'], {'sg_status_list':'rev'})

# Upload your media for approvial
sg.upload('Version', version['id'], '/shotgun/media/checkerboard/checkerboard.mov', 'sg_uploaded_movie')
