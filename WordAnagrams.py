import collections
word = open('words','r') #opens dictionary file
#wordList = word.readlines() #reads lines of dictionary file
#print(wordList[:10])
#wordClean = [word.strip().lower() for word in wordList] #removes /n and makes words lowercase
#print(wordClean[:10])
#wordUnique = list(set(wordClean)) #removes duplicates by putting into a set then back into a list
#print(wordUnique[:10])
#wordUnique.sort() #sorts alphabetically again
#print(wordUnique[:10])
wordClean = sorted(list(set(word.strip().lower() for word in open('words', 'r'))))
#for each line in dictionary file, removes /n and makes lowercase, removes duplicates, alphabetically sorts
#print(wordClean[:10])

def signature(word):
    return ''.join(sorted(word))
#join the sorted letters back into a word

def anagram(myword):
    return[word for word in wordClean if signature(word) == signature(myword)]
#return words whose sorted letters are the same

wordsBySig = collections.defaultdict(list)
#create dict to store sorted letter version of word then all words corresponding. collections package assigns default values

for word in wordClean:
    wordsBySig[signature(word)].append(word)
#fill dict with dictinary words and their sorted versions

def anagramSearch(word):
    return wordsBySig[signature(word)]
#find all words that are anagrams of one another by searching dictionary with sorted letters version
#print(anagramSearch('dictionary'))

anagramsAll = {word: anagramSearch(word) for word in wordList if len(anagramSearch(word)) > 1}
#create dict with word key and all anagrams as values as long as an anagram is not itself
