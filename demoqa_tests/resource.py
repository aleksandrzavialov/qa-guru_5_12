import os


def get_path(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'resources', filename))