# assignment2_mapreduce_REPORT
The requirement of this assignment was to create a search application that retrieves documents similar to an input query. This requirement has been fulfilled through a 2-step process.

Step 1
The purpose of step one was to generate a document containing all the topics present in the input documents, words with their assigned numbers, the frequency of each word in the documents (idf), and the ratio of the frequency of each word to idf. This document facilitates generating answers to queries in step 2. Mapper and reducer scripts were written to create this document. Due to the large size of the input documents and the time required to process them, the input file was initially reduced to 10 documents to expedite output generation and error detection. Inside the mapper script, 'try' and 'except' were used to handle exceptions during file reading, crucial for proper execution on Hadoop. Each line was split based on commas, and the text section retrieved after splitting was further split based on spaces. The output of the mapper file included topics, words, and their article numbers. The reducer file processed this output, separating topics and words and forming dictionaries with words as keys and their counts as values for each document. Using this data, the topic, idf, vocabulary, and tf/idf were printed to the output document.

Step 2
The purpose of step 2 was to retrieve documents matching the input query. Mapper and reducer scripts were again employed, with inputs being the output of step 1 and the query text. The mapper script passed the input directly to the reducer. Inside the reducer, all input data, including idf, vocabulary, and tf/idf dictionaries, were accumulated. The query text was split based on white space, and the resulting words were used to calculate the tf/idf of the query text using the idf and vocabulary dictionaries created earlier. Finally, the inner product of the tf/idf of each document and the query tf/idf was calculated, with a higher inner product indicating greater similarity with the document.

Through these two steps, we created the search application. For optimization purposes, rather than creating an array of the size of the vocabulary length for each document and leaving most indexes as zero, it is more efficient to use a dictionary to store words as keys and their tf/idf values. This reduces the array size and eliminates unnecessary zeros. For example, while testing with 10 documents, the length of an array for a document was around 18500. After successfully running on 10 documents, the program was tested on 5000 documents and then on the entire dataset without encountering any errors. The MapReduce jobs were successful throughout.

to run this project :-
first create a directory inside the hdfs. 
by this command
hadoop fs -mkdir /inputs/

after doing this 
upload the csv file to the hdfs 
hadoop fs -put "path of file" /inputs/

run the indexer by the following command
hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar   -input /inputs/reduced_data.csv  -output /inputs/output1 -mapper mapper.py   -reducer reducer.py   -file /home/i221944/22i-1944/step1_mapper.py   -file /home/i221944/22i-1944/step_1reducer.py

this will create an indexer output documnent which will be stored in the inputs/output1/part-00000

now setup the flask application 

i have given the linkes in it for the step_2 mapper and step_2 reducer, change them accordingly for the working of the application


