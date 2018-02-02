from os import listdir
from nltk import RegexpTokenizer
from nltk import bigrams
from nltk import trigrams
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

#Reading the contents of the folder
def readDirectory(directory):
    content = ""
    for filename in listdir(directory):
        filecontent = open(directory + filename,'r').read()
        content = content + filecontent
    content = content.replace("<br />"," ")
    return content

#Print the number of tokens in the dataset
def printTokenCount(pos_words,neg_words):
    print("................................................................................................")
    print("Total number of words in positive folder: ", len(pos_words))
    print("Total number of words in negative folder: ", len(neg_words))
    print("Total number of word tokens in both folders: ", len(pos_words)+len(neg_words))
    print("................................................................................................")

#Print the number of unique words in the dataset by adding them to a set
def printVocabulary(pos_words,neg_words):
    unique_words = set()
    for i in pos_words:
        unique_words.add(i)
    print("................................................................................................")
    print("Total number of unique words in the positive folder: ",len(unique_words))
    neg_unique = set()
    for i in neg_words:
        unique_words.add(i)
        neg_unique.add(i)
    print("Total number of unique words in the negative folder: ",len(neg_unique))
    print("Total number of unique words in both folders: ",len(unique_words));
    print("................................................................................................")
    return len(unique_words)

#print the top 10 bigrams
def topBigrams(total_words,filtered_words_positive,filtered_words_negative):
    print("................................................................................................")
    print("Top 10 bigrams from positive reviews:")
    frequencies_bigram_positive = FreqDist(bigrams(filtered_words_positive))
    print(frequencies_bigram_positive.most_common(10))
    print("................................................................................................")
    print("Top 10 bigrams from negative reviews:")
    frequencies_bigram_negative = FreqDist(bigrams(filtered_words_negative))
    print(frequencies_bigram_negative.most_common(10))
    print("................................................................................................")
    frequencies_bigram_total = FreqDist(bigrams(total_words))
    print("Top 10 bigrams from both directories: ")
    print(frequencies_bigram_total.most_common(10))
    print("................................................................................................")

#print the top 10 trigrams
def topTrigrams(total_words,filtered_words_positive,filtered_words_negative):
    print("................................................................................................")
    print("Top 10 trigrams from positive reviews:")
    frequencies_trigram_positive = FreqDist(trigrams(filtered_words_positive))
    print(frequencies_trigram_positive.most_common(10))
    print("................................................................................................")
    print("Top 10 trigrams from negative reviews:")
    frequencies_trigram_negative = FreqDist(trigrams(filtered_words_negative))
    print(frequencies_trigram_negative.most_common(10))
    print("................................................................................................")
    print("Top 10 trigrams from both directories:")
    frequencies_trigram_total = FreqDist(trigrams(total_words))
    print(frequencies_trigram_total.most_common(10))
    print("................................................................................................")
    return frequencies_trigram_total

#Function to compute the probability of trigram
def computeProbability(user_input,frequencies_trigram_total,V):
    user_input = user_input.lower()
    trigram_input = user_input.split(' ')
    total_trigrams = sum(frequencies_trigram_total.values())
    denominator = total_trigrams + V
    numerator = frequencies_trigram_total[tuple(trigram_input)] + 1
    return (numerator/denominator)

#MAIN STARTING

#Reading the contents of the files from both folders
positive = readDirectory("Pos/")
negative = readDirectory("Neg/")

#Remove the punctuations, tokenize, convert all to lower case
tokenizer = RegexpTokenizer(r'\w+')
pos_words = tokenizer.tokenize(positive.lower())
neg_words = tokenizer.tokenize(negative.lower())

#Print token and vocabulary size
printTokenCount(pos_words,neg_words)
V = printVocabulary(pos_words,neg_words)

#Remove the stop words
stop_words = set(stopwords.words('english'))
filtered_words_positive = [w for w in pos_words if not w in stop_words]
filtered_words_negative = [w for w in neg_words if not w in stop_words]
total_words = filtered_words_positive + filtered_words_negative

#print top 10 bigrams and trigrams
topBigrams(total_words,filtered_words_positive,filtered_words_negative)
frequencies_trigram_total = topTrigrams(total_words,filtered_words_positive,filtered_words_negative)

#get user input in stdin
print("................................................................................................")
ask = 'y'
while ask=='y':
    print("Enter the input trigram")
    user_input = input()
    print('The probability using add-one smoothing is {0:1.10f}'.format(computeProbability(user_input,frequencies_trigram_total,V)))
    print("Do you want to compute another trigram probability? (y/n)")
    ask = input()
