import googlesearch
import os

error = ""
URL = error
count = 0 

for j in googlesearch.search(URL, stop=10):
    if "stackoverflow" in j and count < 3:
        print(j)
        count += 1
    




