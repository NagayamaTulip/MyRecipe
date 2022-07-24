#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何ポイントを作成しますか？")
print("今日の" + num + "色グラデーションです。")

j = 1

for i in range(0, int(num)):
    r_col = random.sample(range(0, 255), 1)[0]
    g_col = random.sample(range(0, 255), 1)[0]
    b_col = random.sample(range(0, 255), 1)[0]
    
    pos = random.sample(range(0, 100), 1)[0]

    print(str(j) + "ポイント目：" + " R：" + str(r_col) + " G：" + str(g_col) + " B：" + str(b_col) + " ⇒ " + str(pos) + "％")    
    j = j + 1


# In[ ]:




