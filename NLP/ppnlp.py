import nltk                                             #import nltk library suite
nltk.download('punkt')
from nltk.tokenize import sent_tokenize,word_tokenize   #for tokenizing words or sentences
import matplotlib.pyplot as plt                         # for plotting
from nltk.probability import FreqDist                   # for frequncy distribution
from nltk.corpus import stopwords                       # for removing stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer                     # for stemming words
from nltk.stem.wordnet import WordNetLemmatizer         # for lemmatizing words
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')             # for POS tagging


# let's tokenize the text into sentence
text="""Hello Mr. Fernando, how are you doing today? The weather is great, and city is awesome.
The sky is blue. You shouldn't eat from the food truck"""

tokenized_text=sent_tokenize(text)
print(tokenized_text)

#let's tokenize this into words
tokenized_word=word_tokenize(text)
print(tokenized_word)

#now let's check the frequency distribution of these words
fdist = FreqDist(tokenized_word)
print(fdist)

print(fdist.most_common(2))

# now let's generate the frequency Distribution Plot
# import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()


##Let's remove stopwords from the list
# first we create a list of stop words then filter out a list of tokens from these words.

stop_words=set(stopwords.words("english"))
print(stop_words)

#filter a list of tokens from these words
filtered_sent=[]
for word in tokenized_word:
    if word not in stop_words:
        filtered_sent.append(word)

print("tokenized sentence:",tokenized_word)
print("filtered sentence",filtered_sent)


##Lexicon normalization
#stemming
#Stemming is a process of linguistic normalization, which reduces words to their word root or chops off the derivational affixes
ps = PorterStemmer() #create a stemmer object

stemmed_words=[]

for word in filtered_sent:
    stemmed_words.append(ps.stem(word))

print("Filtered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)    

#lemmatization
# Lemmatization reduces words to their base word, which is a linguistically correct lemma.
lem = WordNetLemmatizer()
stem = PorterStemmer()

word = "working"

print("Lemmatized Word:",lem.lemmatize(word,"v"))
print("Stemmed Word:",stem.stem(word))

##POS tagging
sent = "Albert Einstein was born in Ulm, Germany in 1879."

tokens=nltk.word_tokenize(sent)
print(tokens)

pos_tokens = nltk.pos_tag(tokens)
print("POS tagged:",pos_tokens)

