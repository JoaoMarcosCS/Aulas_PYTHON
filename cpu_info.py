from typing import Counter
import psutil


#numeros de cores
print("Physical cores: ",psutil.cpu_count(logical=False))
print("Total cores: ",psutil.cpu_count(logical=True))

#frequencia da CPU
cpufreq=psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")

#Uso da CPU

print("CPU usage per core")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU usage: {psutil.cpu_percent()}%")