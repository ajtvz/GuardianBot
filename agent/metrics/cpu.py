from psutil import cpu_percent
def collect_cpu():
    return cpu_percent(interval=1)