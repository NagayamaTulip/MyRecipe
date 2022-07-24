#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def tag():
    tag = ["work", "experiment", "room", "home", "walking", "science", "lifestyle", "city", "park",
          "color", "nature", "dynamics", "sea", "summer", "neon", "urban", "fireworks", "light", "flower",
          "forest", "spectral", "world", "architecture", "rainbow", "tulip"]
    return random.choice(tag)
title = tag()

h_col = random.sample(range(0, 360), 1)[0]
s_col = random.sample(range(0, 100), 1)[0]
b_col = random.sample(range(0, 100), 1)[0]

print("H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col) + " ⇒ " + title)

for i in range(0, 2):
    shape = random.sample(range(3, 10), 1)[0]
    angle = random.sample(range(0, 360), 1)[0]
    
    h_col = random.sample(range(0, 360), 1)[0]
    s_col = random.sample(range(0, 100), 1)[0]
    b_col = random.sample(range(0, 100), 1)[0]
    
    print(str(shape) + "角形：" + str(angle) + "°回転 ⇒ H：" + str(h_col) + " S：" + str(s_col) + " B：" + str(b_col))


# In[ ]:




