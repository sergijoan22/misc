from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))


# to obtain size info
from win32api import GetSystemMetrics

print("Width:",GetSystemMetrics(0), "px")
print("Height:", GetSystemMetrics(1), "px")

input()