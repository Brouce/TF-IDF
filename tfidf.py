from nltk import word_tokenize
import numpy as np
import math
from string import maketrans
symbols=",[]();:<>+=&+%!@#~?{}|1234567890'"
whitespace='                                 '

def tfidf(word,list):
    termfreq=np.array([])
    tcountindoc=np.array([])
    for document in list:
        doc=word_tokenize(document)
        trans=maketrans(symbols,whitespace)
        doc=str(doc)
        x=doc.translate(trans)
        x=x.strip()
        termcount=doc.count(word)
        if termcount==0:
            continue
        else:
            termfrequency=float(float(termcount)/(len(doc)))
            termfreq=np.append(termfreq,termfrequency)
            tcountindoc=np.append(tcountindoc,termcount)
    idf=math.log(len(list))/(1+len(tcountindoc))
    return(termfreq*idf,tcountindoc)
    
#the function operates on documents which are actually strings, so its a list of strings.
# simple adjustment can be made to import text files.
            

        