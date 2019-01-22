import platform
import sys
import os

mem = str(os.popen('free -t -m').readlines())
T_ind=mem.index('T')
mem_G=mem[T_ind+14:-4]
S1_ind=mem_G.index(' ')
mem_T=mem_G[0:S1_ind]
print(T_ind)

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"

print("""Python version: %s
dist: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))