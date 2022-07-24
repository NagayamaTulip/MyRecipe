#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何種類の組み合わせを作成しますか？")
pattern = input("何パターンを作成しますか？")

for j in range(0, int(pattern)):
    for i in range(0, int(num)):
        shape = random.sample(range(3, 10), 1)[0]
        angle = random.sample(range(0, 360), 1)[0]
        print(str(j + 1) + "番目のパターン ⇒ " + str(shape) + "角形：" + str(angle) + "°回転")
        
for i in range(0, int(num) * int(pattern)):
    r_col = random.sample(range(0, 255), 1)[0]
    g_col = random.sample(range(0, 255), 1)[0]
    b_col = random.sample(range(0, 255), 1)[0]
    
    print("R：" + str(r_col) + " G：" + str(g_col) + " B：" + str(b_col))  


# In[ ]:




