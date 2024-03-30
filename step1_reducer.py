#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys

# Define a set to store unique values
diction = set()
tf_documents = {} #it is a dictionary of dictionaries, it will store the words related to each document sepeartely
topics = {}

list = []
for line in sys.stdin:
    try:
        data = line.strip().split('\t') #splitting 
        
        if data[0] == "topic":
            name = data[1]+"\t"+data[2]  #article_id + name_of_article
            list.append(name)
                
                
        else:
            
            index = data[0]  #index will be having the article id
                    
            if index in tf_documents:  #storing the words in each dictionary. each article id has a seperate dictionary .
                                       #all the article id dictionaries are held in the tf_documents
                inside_diction = tf_documents[index]
                if data[1] in inside_diction:
                    inside_diction[data[1]] +=1
                else:
                    inside_diction[data[1]] = 1
            
                tf_documents[index] = inside_diction
            
            else:
                inside_diction = {}
                inside_diction[data[1]] = 1
                tf_documents[index] = inside_diction
            
            
            # Add data to the set
            diction.add(data[1]) # this set will store all the unique words present in all the documents 
    except Exception as e:
        pass



#the topics are being printed to the output file
list = set(list)
for l in list:
    print(f"topic\t{l}")
    
list = []
    

#a number is assigned to each of the word in the diction
vocabulary = {}
# Print the unique values
for j, key in enumerate(diction):
    vocabulary[key] = j
    

#the orignal word and the number assigned to it are printed to the output file    
for v in vocabulary:
    print(f"vocab\t{v}\t{vocabulary[v]}")



#the tf_documnets, which was a dictionary helding all the dictionaries of the words of each articles, is modiefied to store the numbers assigned to 
#to each word
for key in tf_documents:
    inside_diction = tf_documents[key]
    new_diction = {}
    for k in inside_diction:
        if k in vocabulary:
            value = vocabulary[k]
            data = inside_diction[k]
            new_diction[value] = data
            
            
    tf_documents[key] = new_diction
    
        

#the term documents frequencies of each word are being find out in this ; no of documents in which the word appear
idf_diction = {}
for term in vocabulary:
    data = vocabulary[term]
    
    for key in tf_documents:
        inside_diction = tf_documents[key]
        
        if data in inside_diction:
            if data in idf_diction:
                idf_diction[data] += 1
            else:
                idf_diction[data] = 1
            

#the term frequencies are being printed to the documents
for key in idf_diction:
    print(f"idf\t{key}\t{idf_diction[key]}")
 

   

# TF/IDF
tf_idf_diction = {}

for key in tf_documents:
    inside_diction = tf_documents[key]
    document_diction = {}
    for k in inside_diction:
        tf_value = inside_diction[k] # frequency of the word in all the documnets
        idf_value = idf_diction[k] # frequency of documnets in which the word appear
        
        vectore_value = tf_value/idf_value
        vectore_value = round(vectore_value,2)
        document_diction[k] = vectore_value
        
    tf_idf_diction[key] = document_diction
    


#key :- document no , l :- word , tf/idf value
for key in tf_idf_diction:
    # print(f"index {key}\n")
    inside_diction = tf_idf_diction[key]
    for l in inside_diction:
        print(f"tf_idf\t{key}\t{l}\t{inside_diction[l]}")
        






  
   