# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:18:51 2020

@author: JP
"""

""" 
This code does stuff. trial code for use in Github to see how Github works.
"""


class timefix:
    """
    a sample code to handle two different time related adjustments.
    this is just to test out classes and Github.
    """
    def __init__(self, t):
        pass
    
    def time_text(t):
        """
        time_text(time)
        Takes the time in a text string field in variousa formats 736, 0736, 07:36, 07-36
        and then converts it to a simple four digit time string '0736'
        """
        
        ts= t.replace(":", "").replace("-", "")
        if len(ts) == 4:
            return ts
        elif len(ts) ==3:
            t2 = "0" + ts
            return t2
        elif len(ts) ==2:
            t3 = "00" + ts
            return t3
        elif len(ts) ==1:
            t4 = "000" + ts
            return t4
        else:
            return "-"

        
    def time_int(t):
        """
        time_int(time)
        Takes the time from an interger field in various formats 736, 36
        and then converts it to a simple four digit time string '0736' or '0036'
        """
        
        ts= str(t)
        if len(ts) == 4:
            return ts
        elif len(ts) ==3:
            t2 = "0" + ts
            return t2
        elif len(ts) ==2:
            t3 = "00" + ts
            return t3
        elif len(ts) ==1:
            t4 = "000" + ts
            return t4
        else:
            return "-"