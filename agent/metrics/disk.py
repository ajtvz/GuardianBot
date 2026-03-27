from psutil import disk_usage

def collect_disk():
    disk = disk_usage('/')
    return {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }