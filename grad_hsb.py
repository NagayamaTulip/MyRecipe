#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何ポイントを作成しますか？")
print("今日の" + num + "色グラデーションです。")

j = 1

for i in range(0, int(num)):
    h_col = random.sample(range(0, 360), 1)[0]
    s_col = random.sample(range(0, 100), 1)[0]
    b_col = random.sample(range(0, 100), 1)[0]
    
    pos = random.sample(range(0, 100), 1)[0]

    print(str(j) + "ポイント目：" + " H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col) + " ⇒ " + str(pos) + "％")
    j = j + 1


# In[ ]:




