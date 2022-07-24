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
    h_col = random.sample(range(0, 360), 1)[0]
    s_col = random.sample(range(0, 100), 1)[0]
    b_col = random.sample(range(0, 100), 1)[0]
    
    print("H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col))  


# In[ ]:




