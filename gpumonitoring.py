import pynvml

pynvml.nvmlInit()
device_count = pynvml.nvmlDeviceGetCount()

for i in range(device_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    print("GPU", i, ":")
    print("    Name:", pynvml.nvmlDeviceGetName(handle))
    print("    Temperature:", pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU), "C")
    print("    Memory Usage:", pynvml.nvmlDeviceGetMemoryInfo(handle).used / 1024**2, "MB")
    print("    Utilization:", pynvml.nvmlDeviceGetUtilizationRates(handle).gpu, "%")

pynvml.nvmlShutdown()
