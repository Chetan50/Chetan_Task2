#!/usr/bin/env python
# coding: utf-8

# In[ ]:


text = input()
letter = input()
text_count = 0
letter_count = 0
for i in text:
    text_count += 1
for i in text:
    if letter == i:
        letter_count += 1
letter_percentage = (letter_count/text_count)*100        
print(int(letter_percentage))

