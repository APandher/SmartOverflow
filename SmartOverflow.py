import googlesearch
import os

class SmartOverflow:

    def __init__(self):
        try:

        except exception as x:
            smart_except(x)
            
    
    def smart_except(self,x):
   
        error = x
        URL = str(error)
        count = 0 

        for j in googlesearch.search(URL, stop=10):
            if "stackoverflow" in j and count < 3:
                print(j)
                count += 1
 



