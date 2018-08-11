
# coding: utf-8

# ## read inputDataFile of a string containg sentences of a subtitle 

# In[1]:


with open ("/home/sarkijatru/Desktop/srikarProject/usingLex/normal/data.txt", "r") as myfile:
    data=myfile.readlines()


# # preprocessing
# 
# ## Replace shortWord with original form

# In[2]:


contractions = {
"ain't": "am not / are not",
"aren't": "are not / am not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he had / he would",
"he'd've": "he would have",
"he'll": "he shall / he will",
"he'll've": "he shall have / he will have",
"he's": "he has / he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has / how is",
"i'd": "I had / I would",
"i'd've": "I would have",
"i'll": "I shall / I will",
"i'll've": "I shall have / I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it had / it would",
"it'd've": "it would have",
"it'll": "it shall / it will",
"it'll've": "it shall have / it will have",
"it's": "it has / it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had / she would",
"she'd've": "she would have",
"she'll": "she shall / she will",
"she'll've": "she shall have / she will have",
"she's": "she has / she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so as / so is",
"that'd": "that would / that had",
"that'd've": "that would have",
"that's": "that has / that is",
"there'd": "there had / there would",
"there'd've": "there would have",
"there's": "there has / there is",
"they'd": "they had / they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they shall have / they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had / we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what shall / what will",
"what'll've": "what shall have / what will have",
"what're": "what are",
"what's": "what has / what is",
"what've": "what have",
"when's": "when has / when is",
"when've": "when have",
"where'd": "where did",
"where's": "where has / where is",
"where've": "where have",
"who'll": "who shall / who will",
"who'll've": "who shall have / who will have",
"who's": "who has / who is",
"who've": "who have",
"why's": "why has / why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had / you would",
"you'd've": "you would have",
"you'll": "you shall / you will",
"you'll've": "you shall have / you will have",
"you're": "you are",
"you've": "you have"
}


# In[3]:


for word in data[0].split():
    if word.lower() in contractions:
        #data[0] = data[0].replace(word, contractions[word.lower()])
        ##edited on 11/8/18
        data[0] = data[0].replace(word,"")


# ### regexp to replace / with space''

# In[4]:


import re
data[0]= re.sub(r'/', " ", data[0])


# ## split string  to get words

# In[5]:


dataArray=data[0].split()
len(dataArray)


# # Remove stopwords

# In[6]:


from nltk.corpus import stopwords
s=set(stopwords.words('english'))
### Remove stop words
wordsWithoutStopWords=list(filter(lambda w: not w in s,dataArray))
len(wordsWithoutStopWords)

###Conclusion
#(5950-3254)=2696 stopWords removed

### 10/8/18
## 5950-3274=2676  removed
# 5902-3226=2676


# ## read commonWords from file

# In[7]:


with open('/home/sarkijatru/Desktop/srikarProject/commonWords.txt', 'r') as myfile1:
    data1=myfile1.read().replace('\n', ' ')# read file a replace newLine with space so that split can be performed


# # generate all possible forms of word from commonWords 
# ## and
# # Remove common words 

# In[8]:


commonWordsArray=data1.split()
commonWordsArray=[x.upper() for x in commonWordsArray] #capitalize'em

wordsWithoutStopWords=[x.upper() for x in wordsWithoutStopWords] #capitalize'em

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

lemmatizer = WordNetLemmatizer()

import inflect
p = inflect.engine()

forms = set() #We'll store the derivational forms in a set to eliminate duplicates
for commonWord in commonWordsArray:
    for word in wn.lemmas(commonWord): #for each commonWord lemma in WordNet
        forms.add(word.name()) #add the lemma itself
        for relatedWord in word.derivationally_related_forms(): #for each related lemma
            forms.add(relatedWord.name()) #add the related lemma\

    for word in wn.lemmas(lemmatizer.lemmatize(commonWord)):
        forms.add(word.name()) #add the lemma itself
        for relatedWord in word.derivationally_related_forms(): #for each related lemma
            forms.add(relatedWord.name()) #add the related lemma\

    for word in wn.lemmas(ps.stem(commonWord)):
        forms.add(word.name()) #add the lemma itself
        for relatedWord in word.derivationally_related_forms(): #for each related lemma
            forms.add(relatedWord.name()) #add the related lemma\

    forms.add(lemmatizer.lemmatize(commonWord))
    forms.add(commonWord)
    forms.add(ps.stem(commonWord))
    forms.add(p.plural(commonWord))
    
forms=[x.upper() for x in forms]# capitalize'emforms=[x.upper() for x in forms]# capitalize'em

wordsWithoutCommonWordsAndItsForms=list(filter(lambda w: not w in forms,wordsWithoutStopWords))


# In[9]:


len(wordsWithoutCommonWordsAndItsForms)
###conclusion :9/8/18 :thursday 
# 3254-1650=1604 common words removed

###10/8/18 friday
# 3254-1409=1845 common words removed

# 3 things added
# 3274-1443=1831 removed

###11/8/18
# inflect plurals
# 3274-1333=1941 removed


# In[10]:


finalWordSet=set()
for i in range(len(wordsWithoutCommonWordsAndItsForms)):
    finalWordSet.add(wordsWithoutCommonWordsAndItsForms[i])


# In[11]:


finalWordSet


# In[12]:


len(finalWordSet)

