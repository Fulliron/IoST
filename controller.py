import pickle, os
from Device import *

keys = {}
devices = {}
current_permission = 0
max_level_permission = 5
current_device = Device("none", max_level_permission, lambda: None)

def add_device(name, level, purpose):
    devices.append(Device(name, level, purpose))

def allow_run(level, device):
    if device in devices:
        if level == max_level_permission:
            return device.run
        else:
            if device.perms(level):
                return device.run
            else:
                print("Insufficient permissions. Please ask a parent for help.")
    else:
        print("Device not installed. Please install the device, or select an already installed device.")

def select_device():
    nonlocal current_permission, current_device, devices
    print("Please select a device from the list below:")
    active = [dev.append() for dev in devices.keys() if devices[dev].perms(current_permission)]
    user_input = input("")
    if user_input in active:
        current_device = devices[user_input]
    elif user_input in devices:
        print("You do not have permission for this device. Please get help if you need to access it.")
    else:
        print("This device is not installed. Please install it.")

def set_perms(key):
    """Sets current permission level"""
    nonlocal current_permission
    if key in keys.keys():
        current_permission = keys[key]
    else:
        print ("Key not accepted.")

def save_and_exit():
    """Saves the dictionary of keys and the list of devices,  and safely shuts down the controller. If the directory does not exist, create it."""
    nonlocal keys
    def save(obj, name):
        try:
            with open('%HOMEDRIVE%\%HOMEPATH%/lists/'+ name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError:
            os.mkdir("%HOMEDRIVE%\%HOMEPATH%/keys")
            save(obj, name)
    save(keys, "keys")
    save(devices, "devices")
    exit()   
        
def loader():
    """On load, loads lists from file if they exist; else, creates the save directory"""
    keys = load("keys")
    devices = load("devices")

"""Helper functions for file manipulation"""
def load(name):
        try:
            with open('%HOMEDRIVE%\%HOMEPATH%/lists/' + name + '.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            os.mkdir("%HOMEDRIVE%\%HOMEPATH%/lists")

def save(obj, name):
        try:
            with open('%HOMEDRIVE%\%HOMEPATH%/lists/'+ name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        except FileNotFoundError:
            os.mkdir("%HOMEDRIVE%\%HOMEPATH%/lists")
            save(obj, name)
    


