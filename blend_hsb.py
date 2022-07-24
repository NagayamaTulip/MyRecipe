#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

step = random.sample(range(2, 7), 1)[0]
print("ステップ数は、" + str(step) + "です。")

for i in range(0, 2):
    shape = random.sample(range(3, 10), 1)[0]
    angle = random.sample(range(0, 360), 1)[0]
    
    h_col = random.sample(range(0, 360), 1)[0]
    s_col = random.sample(range(0, 100), 1)[0]
    b_col = random.sample(range(0, 100), 1)[0]
    
    print(str(shape) + "角形：" + str(angle) + "°回転 ⇒ H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col))


# In[ ]:




