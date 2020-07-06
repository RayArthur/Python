import os

dir = "myDir"

if not os.path.exists(dir):
    os.mkdir(dir)
    print(dir + "建立成功!")
else:
    print(dir + "已經建立!")   
 