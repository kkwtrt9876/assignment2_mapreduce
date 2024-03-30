#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys

vocabulary = {}
tf_idf_diction = {}
query_data = {}
topic = {}
idf_diction = {}
inner_products = {}


for line in sys.stdin:  #all the data comming through the stdin is stored in the relevant dictionaries
    data = line.split('\t')
    if data[0] == "vocab":
        vocabulary[data[1]] = int(data[2])
        
    elif data[0] == "tf_idf":
        if data[1] in tf_idf_diction:
            lis = tf_idf_diction[data[1]] #done the changing to float in this step
            lis[data[2]] = data[3]
            tf_idf_diction[data[1]] = lis
        else:
            lis = {}
            lis[data[2]] = data[3]
            tf_idf_diction[data[1]] = lis
            
            
    elif data[0] == 'topic':
        topic[data[1]] = data[2]
        
    elif data[0] == "idf":
        
        idf_diction[int(data[1])] = int(data[2])            
    else:
        
        for d in data:
            lines = d.split()  #the query data is converted and split in to words and stored
            for l in lines:
                if l in query_data:
                    query_data[l] +=1
                else:
                    query_data[l] = 1
                    
            
            


query_tf_idf = {}

# the words of the querry data are now converted into numbers
new_query = {} 

for key in query_data:
    if key in vocabulary:
        new_query[vocabulary[key]] = query_data[key]
        
query_data = {}

        

#the tf/idf values of the query are being identified        
        
for data in new_query:
    tf_value = int(new_query[data])
    
    idf_value = int(idf_diction[data])
    
    
    score = tf_value/idf_value
    score = round(score,2)
    query_tf_idf[data] = score
    



result_list = []


for key in tf_idf_diction:
    
    inside_diction = tf_idf_diction[key]
    score = 0
    for data in query_tf_idf:
        # print(f"query ==> {type(query_tf_idf[data])}")
        str_data = str(data)
        if str_data in inside_diction:
            value1 = query_tf_idf[data]
            value2 = inside_diction[str_data]
            value2 = float(value2)
            
            
            score += (value2*value1)
       
        
    
            
            
    
    inner_products = round(score,2)
    result_list.append((key, inner_products))
    
result_list.sort(key=lambda x: x[1], reverse=True)


topics_print = []

for key, inner_product in result_list:
    print(f"{key} ==> {inner_product}")
    topics_print.append(key)
 

print("\nthe most relevant documents :- ")   

for key in topics_print:
    print(f"{topic[key]}")
    
    