import psutil
import time

_last_net = None
_last_time = None

def collect_network():
    global _last_net, _last_time

    current = psutil.net_io_counters()
    now = time.time()

    if _last_net is None:
        # First run — no previous data to compare
        _last_net = current
        _last_time = now
        return {
            "bytes_sent_per_sec": 0,
            "bytes_recv_per_sec": 0
        }

    # Calculate deltas
    time_diff = now - _last_time
    sent_per_sec = (current.bytes_sent - _last_net.bytes_sent) / time_diff
    recv_per_sec = (current.bytes_recv - _last_net.bytes_recv) / time_diff

    # Update stored values
    _last_net = current
    _last_time = now

    return {
        "bytes_sent_per_sec": sent_per_sec,
        "bytes_recv_per_sec": recv_per_sec
    }