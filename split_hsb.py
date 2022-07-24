#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

tate = random.sample(range(1, 7), 1)[0]
yoko = random.sample(range(1, 12), 1)[0]

def shape():
    shape = ["四角", "丸"]
    return random.choice(shape)
select = shape()

print("横： " + str(yoko) + "個、縦： " + str(tate) + "に分割 ⇒ " + select + "を選択")

num = input("何個に色を付けますか？")

for i in range(0, int(num)):
    h_col = random.sample(range(0, 360), 1)[0]
    s_col = random.sample(range(0, 100), 1)[0]
    b_col = random.sample(range(0, 100), 1)[0]
    
    print("H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col)) 

