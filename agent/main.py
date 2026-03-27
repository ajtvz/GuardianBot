from agent import device_id
from agent.metrics import collect_all_metrics
from agent.device_id import get_device_id
import time
def start ():
    device_id = get_device_id()
    start_time = time.time()
    while True:
        if time.time() - start_time >= 30:  # Run for 30 seconds
            print("Done")
            break
        metrics = collect_all_metrics()
        timestamp = int(time.time())
        payload = {
            'device_id': device_id,
            "timestamp": int(timestamp),
            "metrics": metrics
        }
        print(payload)
        time.sleep(1)  # Sleep for a short time to avoid busy waiting
if __name__ == "__main__":
    start()
        