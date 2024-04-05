import spacy    #Natural language library 
import json #a #for Working with JSON data
import requests #a  #for sending HTTP requests
import gensim #a #for text summarization
from spacy.lang .en.stop_words import STOP_WORDS #for removing stopwords
from string import punctuation  #for removing punctuations
from data import dataT #a 
from heapq import nlargest 


#The Main fuction to summarize the text
def summarizer(rawdocs):
        #data Preperation Starts Here
        #Loads English language model in spacy
        stopwords = list (STOP_WORDS)
        #print(stopwords)
        nlp = spacy.load('en_core_web_sm')
        doc = nlp (rawdocs)
        #print(doc)        
        
        
        #Word Tokenization: Tokenization is the process of breaking the text into smaller parts called tokens
        tokens = [token.text for token in doc]
        #print (tokens)
        print(dataT["size"]) #a
        size=dataT["size"] #a
        url=dataT["url"] #a
        headers = dataT["headers"] #a
        payload = {
            "providers": dataT["a"],
            "output_sentences": size,
            "language": "en",
            "text": rawdocs,
            "fallback_providers": ""
        } #a
        #data Preperation Ends Here
        
        
        #Calculating the Wrequency of words in the text: with removing StopWords and Punctuations
        word_freq ={}
        for word in doc:
            if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else: 
                    word_freq[word.text] += 1
        #print(word_freq)
        max_freq =max(word_freq.values())
        #print (max_freq)
        
        
        #Frequence Normalization: By deviding each frequency by maximum frequency
        for word in word_freq.keys():
            word_freq[word] = word_freq[word]/max_freq
        #print(word_freq)
        #frequency of words ends here
        
        
        #Sentence tokenization: Using spacy
        sent_tokens = [sent for sent in doc.sents]
        #print (sent_tokens)
        #Sentence tokenization ends here
        
        
        #Sentence Scoring: Calculating the score of each sentence by adding the frequency of the words that are present in the sentence
        sent_scores = {}
        for sent in sent_tokens:
            for word in sent :
                if word.text in word_freq.keys():
                    if sent not in sent_scores.keys():
                        sent_scores[sent] = word_freq[word.text]
                    else:
                        sent_scores[sent] += word_freq[word.text]
        #print(sent_scores)
        #Sentence Scoring ends here
        
        
        #Summary Creation: Selecting 30% of the sentences having the highest scores.
        select_len = int (len (sent_tokens) * 0.3)
        #print(select_len)
        summary = nlargest(select_len,sent_scores,key=sent_scores.get)
        #print(summary)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        # print (text)
        # print(summary)
        # print("Length of original text ",len(text.split(' ')))
        # print("Length of summary text ",len(summary.split(' ')))
        
        #gensim Working Starts: Using Gensim for Text Summarization for Abstractive Summarazation.
        response = requests.post(url, json=payload, headers=headers) #a

        json_data = json.loads(response.text) #a
        # Parse the JSON data
        # Extract the summary
        summary =     summary = json_data[dataT["a"]]["result"]
        # print(json_data) #a
        return summary,rawdocs,len(rawdocs.split(' ')),len(summary.split(' ')) #a


# def summarizer(rawdocs):
#     print(summary)
#     print(rawdocs)
#     return summary,rawdocs,len(rawdocs.split(' ')),len(summary.split(' '))
# summarizer("A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations (computation) automatically. Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation; or to a group of computers that are linked and function together, such as a computer network or computer cluster.")