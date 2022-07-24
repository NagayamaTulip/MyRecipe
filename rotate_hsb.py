#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何回、繰り返しますか？")

shape = random.sample(range(3, 10), 1)[0]
angle = random.sample(range(0, 360), 1)[0]
free = random.sample(range(-200, 200), 1)[0]
    
print(str(shape) + "角形：" + str(angle) + "°回転、" + str(free) + "％収縮・膨張")

rotate = int(180 / int(num))
print(str(rotate) + "°回転に設定してください。")
        
for i in range(0, int(num)):
    h_col = random.sample(range(0, 360), 1)[0]
    s_col = random.sample(range(0, 100), 1)[0]
    b_col = random.sample(range(0, 100), 1)[0]
    
    print("H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col)) 


# In[ ]:




