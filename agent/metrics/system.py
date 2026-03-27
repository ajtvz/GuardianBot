import platform
import socket
import psutil
import time

def collect_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "boot_time": psutil.boot_time(),
        "cpu_count": psutil.cpu_count(logical=True),
        "cpu_physical": psutil.cpu_count(logical=False)
    }
