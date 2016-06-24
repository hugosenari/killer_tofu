import os

STATIC_FOLDERS = (
    'killer_tofu/common/static',
    'killer_tofu/users/static',
)

# Muffin Plugins
PLUGINS = (
    'muffin_jinja2',
    'muffin_peewee',
    'muffin_session',
)


# Plugins configurations
SESSION_SECRET = 'SecretHere'
SESSION_LOGIN_URL = '/users/signin/'

JINJA2_TEMPLATE_FOLDERS = (
    'killer_tofu/common/templates',
    'killer_tofu/public/templates',
    'killer_tofu/users/templates'
)

PEEWEE_CONNECTION = os.environ.get('DATABASE_URL', 'sqlite:///killer_tofu.sqlite')
