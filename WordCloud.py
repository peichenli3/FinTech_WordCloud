
# pip install -U spacy
# python -m spacy download en_core_web_lg

import os
import spacy
import docx2txt             # A pure python-based utility to extract text from docx files.
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import en_core_web_lg
import pandas as pd
import numpy as np
# import sys
# clear all vars for rerun
# sys.modules[__name__].__dict__.clear()

# set the working directory
os.chdir("C:\\Users\\90596\\Desktop\\WordCloud_spaCy")
# import the docx file and apply spaCy nlp to it to extract the text
text = docx2txt.process("both.docx")
nlp = en_core_web_lg.load()
doc = nlp(text)

# Generate tokens without filtering
list1 = []
for token in doc:
    if not token.is_punct:                 # filter out tokens of punctuations
        print(token, token.lemma, token.lemma_)
        list1.append( token.lemma_ )

# Remove '-PRON-' and transform 'datum' to 'data'
list1 = [x for x in list1 if x != '-PRON-']
for i, word in enumerate(list1):
    if word == 'datum':
        list1[i] = 'data'

# Write list1 to a DF and list1.csv file
df = pd.DataFrame(list1, columns=["colummn"])
df.to_csv('list1.csv', index=False)

# Import the stop words as a list
df = pd.read_csv("tokenize tasks stop words.csv")
matrix2 = df[df.columns[0]].to_numpy()
list2 = matrix2.tolist()
# filtering using file tokenize tasks stop words.csv
list3 = [x for x in list1 if x not in list2]
# filtering using nlp default stop words
list4 = [x for x in list3 if x not in nlp.Defaults.stop_words]

# Write to file list4.csv
df = pd.DataFrame(list4, columns=["colummn"])
df.to_csv('list4.csv', index=False)


# Visualization of cleaning tokens
unique_string=(" ").join(list4)
wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("Fintech"+".png", bbox_inches='tight')
plt.show()
plt.close()

