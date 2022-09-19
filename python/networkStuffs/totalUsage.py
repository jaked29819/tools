import time

UPDATE_DELAY = 1

def get_size(bytes):
    """
    Returns size of data in a nice format
    """

    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


