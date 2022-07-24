#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何パターンを作成しますか？")

for i in range(0, int(num)):
    shape = random.sample(range(3, 10), 1)[0]
    angle = random.sample(range(0, 360), 1)[0]
    ratio = random.sample(range(0, 100), 1)[0]
    
    print(str(shape) + "角形：" + str(angle) + "°回転、" + str(ratio) + "％縮小コピー")
        
for i in range(0, int(num)):
    r_col = random.sample(range(0, 255), 1)[0]
    g_col = random.sample(range(0, 255), 1)[0]
    b_col = random.sample(range(0, 255), 1)[0]
    
    print("R：" + str(r_col) + " G：" + str(g_col) + " B：" + str(b_col))  


# In[ ]:




