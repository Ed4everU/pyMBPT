from pynvml import *

def get_gpu_info():

    nvmlInit()
    ngpu = nvmlDeviceGetCount()
    driver_version = nvmlSystemGetDriverVersion()
    