from .cpu import collect_cpu
from .disk import collect_disk
from .memory import collect_memory
#from .network import collect_network
#from .system import collect_system

def collect_all_metrics():
    cpu = collect_cpu()
    disk = collect_disk()
    memory = collect_memory()
    #network = collect_network()
    #system = collect_system()
    metrics = {
        "cpu": cpu,
        "disk": disk,
        "memory": memory,
        #"network": network,
        #"system": system,
    }
    return metrics