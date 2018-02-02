Name: Keerthanaa G Saminathan
ID  : 1750117

the python code doesn't take any command line arguments.

python3 keerthanaa_hw1.py

It displays,
1. the total number of tokens in positive and negative folders, the aggregate total number of words
2. Vocabulary size in positive and negative folders, the total vocabulary size
3. Top 10 bigrams in the positive and negative folders, the top 10 bigrams in both the folders together
4. Top 10 trigrams in the positive and negative folders, the top 10 trigrams in both the folders together
5. It then takes a trigram as input in stdin and prints the trigram model probability using add-one smoothing technique

The python code has the following functions
1. readDirectory #Reading the contents of the folder
2. printTokenCount #Print the number of tokens in the dataset
3. printVocabulary #Print the vocabulary size
4. topBigrams #print the top 10 bigrams
5. topTrigrams #print the top 10 trigrams
6. computeProbability #Function to compute the probability of trigram model