from agent.metrics import collect_all_metrics
import time
def start ():
    start_time = time.time()
    while True:
        if time.time() - start_time >= 30:  # Run for 30 seconds
            print("Done")
            break
        metrics = collect_all_metrics()
        payload = {
            "metrics": metrics
        }
        print(payload)
        time.sleep(1)  # Sleep for a short time to avoid busy waiting
if __name__ == "__main__":
    start()
        