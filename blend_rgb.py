#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

step = random.sample(range(2, 7), 1)[0]
print("ステップ数は、" + str(step) + "です。")

for i in range(0, 2):
    shape = random.sample(range(3, 10), 1)[0]
    angle = random.sample(range(0, 360), 1)[0]
    
    r_col = random.sample(range(0, 255), 1)[0]
    g_col = random.sample(range(0, 255), 1)[0]
    b_col = random.sample(range(0, 255), 1)[0]
    
    print(str(shape) + "角形：" + str(angle) + "°回転 ⇒ R：" + str(r_col) + " G：" + str(g_col) + " B：" + str(b_col))


# In[ ]:




