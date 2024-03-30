#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
import csv


article_id = 0

title = "TITLE"

data = {}


for line in sys.stdin:
    try:
        
        data = line.strip().split(',') #splitting on th base of , and removing extra spaces
        to_reduce = data[0].split()  #data[0] has the textcontent ; split on the basis space
        
        for r in to_reduce:
            print(f"{article_id}\t{r}") #prints each word from the text along with the article no , at the start it will be 0
        
        if isinstance(data[1], str): #logic is set over here to update the article no
            try:
                num = int(data[0])
                article_id = num
                
                if data[1] != title:
                    print(f"topic\t{article_id}\t{data[1]}")
                
                
                
            except ValueError:
                
                pass  # Do nothing if conversion fails
            
        
        
    
    except Exception  as e:
        pass
    


    