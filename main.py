import os


def get_source_root():
    current_file = os.path.abspath(__file__)
    source_root = os.path.dirname(current_file)
    return source_root
