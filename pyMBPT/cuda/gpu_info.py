from pynvml import *

def get_gpu_info():

    try: 
        
        nvmlInit()
        ngpu = nvmlDeviceGetCount()
        driver_version = nvmlSystemGetDriverVersion()

        print("NGPU: %d".format(ngpu))
        print("Driver Version: ", driver_version)

        for i in range(ngpu):
            handle = nvmlUnitGetHandleByIndex(i)
            print("Device %d: %s".format(i, nvmlDeviceGetName(handle)))

    except:

        print("GPU can't be used")