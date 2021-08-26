**Input**: a collection of abstracts of papers from financial economists.

**Logistics**:  
1.	Load the dependencies including:  
*	os: setting working directory  
* spacy: apply nlp model  
* docx2txt: a pure python-based utility to extract text from docx files  
* matplotlib: visualization  
* en_core_web_lg: spacy’s nlp model  
* pandas: import the stop words csv to a list  
* numpy  

2.	Set the working directory with files included: both.docx and tokenize tasks stop words.csv (Note that here I transform the initial xlsx file into csv for pandas to read)  

3.	Import our text data both.docx and tokenize it  

4.	Generate a list for tokenized words  

5.	Generate list of a stop words  

6.	Filtering  

7.	Visualization using wordcloud

**Output**:

![](Fintech.png?raw=true)


**Naive conclusion**: to understand the market, data is essential!!
