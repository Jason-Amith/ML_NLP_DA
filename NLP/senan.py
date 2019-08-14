import pandas as pd
import matplotlib.pyplot as plt 
#sentiment label legend
#0 - negative 1 - somewhat negative 2 - neutral 3 - somewhat positive 4 - positive

data=pd.read_csv('train.tsv', sep='\t')
data.head()
data.info
print(data)

data.Sentiment.value_counts()

Sentiment_count=data.groupby('Sentiment').count()
plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
plt.xlabel('Review Sentiments')
plt.ylabel('Number of Review')
plt.show()

##Feature generation : 

#1.Bag of words.
#generate document term matrix by using scikit-learn's CountVectorizer.
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer

#tokenizer to remove unwanted elements from out data like symbols and numbers
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(data['Phrase'])

#2. TF-IDF
# from sklearn.feature_extraction.text import TfidfVectorizer
# tf=TfidfVectorizer()
# text_tf= tf.fit_transform(data['Phrase'])


#split train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    text_counts, data['Sentiment'], test_size=0.3, random_state=1)

#model building and evaluation
from sklearn.naive_bayes import MultinomialNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print(y_test, predicted)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))