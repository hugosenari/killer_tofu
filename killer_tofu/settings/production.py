import os
from .base import LOGGING

STATIC_FOLDERS = (
    'killer_tofu/common/static'
)

# Muffin Plugins
PLUGINS = ('muffin_motor',)

# MONGO
MOTOR_HOST=os.environ.get('MOTOR_HOST', 'killer_tofu_data')
MOTOR_PORT=os.environ.get('MOTOR_PORT', 27017)
MOTOR_DB=os.environ.get('MOTOR_DB', 'killer_tofu')
MOTOR_USERNAME=os.environ.get('MOTOR_USERNAME')
MOTOR_PASSWORD=os.environ.get('MOTOR_PASSWORD')
MOTOR_MAX_POOL_SIZE=os.environ.get('MOTOR_MAX_POOL_SIZE', 1)