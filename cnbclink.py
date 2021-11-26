#!/usr/bin/python3
# coding: utf-8

# In[11]:


from urllib.request import urlopen

html = urlopen("https://www.livenewsnow.com/american/cnbc-america.html")
data = str(html.read())
start = data.find("file: ")
end = data.find(",autostart:")
link = str(data[start+7:end-1])
print(link)
