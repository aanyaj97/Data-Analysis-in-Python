import collections
word = open('words','r') #opens dictionary file

wordClean = sorted(list(set(word.strip().lower() for word in open('words', 'r'))))
#for each line in dictionary file, removes /n and makes lowercase, removes duplicates, alphabetically sorts
#print(wordClean[:10])

'''
Making a dictionary of all anagrams of all words in the English Dictionary
'''
def signature(word):
    return ''.join(sorted(word))
#join the sorted letters back into a word

wordsBySig = collections.defaultdict(list)
#creates dictionary of lists to store sorted letter version of word then all words corresponding

for word in wordClean:
    wordsBySig[signature(word)].append(word)
#fill correct list of signature of a word with the various words that match

def anagramSearch(word): #finds anagrams of a given word
    return wordsBySig[signature(word)]
#find all words that are anagrams of one another by returning the list corresponding to the word's signature
#print(anagramSearch('dictionary'))

anagramsAll = {word: anagramSearch(word) for word in wordClean if len(anagramSearch(word)) > 1}
#create dict with word key and all anagrams as values as long as there is more than one anagram for it besides itself

'''
Finding how many anagrams of each length exist
'''

wordsByLen = collections.defaultdict(list)
#creates dictionary of lists to store words acording to length

for word in wordClean:
    wordsByLen[len(word)].append(word)
#sorts all words by their length into the dictionary of lists. Each list contains words that are all the same length.

def countAnagrams(length): #creates function to count the number of anagrams that exist for given length of word
    count = 0
    for i in wordsByLen[length]:
        count += len(anagramSearch(i)) - 1
    return count/2
#for each member of the list of words that are of the given length, count the number of anagrams it has minus one (itself)
#This counts them twice (i.e. elvis = lives but lives = elvis) so we divide by 2 to get rid of duplicates

anagramsByLenTotal = {}
#creates a dictionary to store length of words and number of corresponding anagrams

for i in range(1,len(wordsByLen)+1):
    anagramsByLenTotal.update({i: countAnagrams(i)})
#adds members to dictionary with key: the length of word, value: number of anagrams

for length, number in anagramsByLenTotal.items():
    print(str(length) + ":" + str(number))
#let us see how many anagrams exist for each length of word! :)
