import os
import uuid

DEVICE_ID_FILE = "device_id.txt"

def get_device_id():
    if os.path.exists(DEVICE_ID_FILE):
        with open(DEVICE_ID_FILE, "r") as f:
            return f.read().strip()

    # Create a new one
    new_id = str(uuid.uuid4())
    with open(DEVICE_ID_FILE, "w") as f:
        f.write(new_id)
    return new_id
if __name__ == "__main__":
    print(get_device_id())


#insures every machine gets a unique id that is stored in a file so it can be reused across runs. This is important for identifying the device when sending metrics to a server.