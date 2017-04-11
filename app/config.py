import os


class Config(object):
    """The default application configuration."""
    SERVER_NAME = os.environ.get('SERVER_NAME', 'app.docker:5042')
