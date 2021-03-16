import time
import uiautomation as auto

Edius = auto.WindowControl(searchDepth = 1, Name = 'EDIUS')
Edius.SetActive()

timeine = Edius.Control(searchDepth = 3, ClassName = 'CtsGuiClass.Window')
if auto.WaitForExist(timeine, 0):
    timeine.SendKeys("{enter}")
    time.sleep(3)
    timeine.SendKeys("{enter}")
    timeine.SendKey(auto.Keys.VK_A)
    timeine.SendKey(auto.Keys.VK_S)

else:
    print("No timeline")

