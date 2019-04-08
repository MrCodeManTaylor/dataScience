#Mitchell Taylor

import math
from math import sqrt
import string
import codecs
#import re


### ONLINE IDE: You can use http://www.tutorialspoint.com/execute_python3_online.php
### Project Gutenberg: https://www.gutenberg.org/ebooks/search/%3Fsort_order%3Ddownloads
import csv
import urllib.request

print('\nNow running comparison algorithms, please wait.\n\n')

### FUNCTION GET LINES: Get the files, either directly online or by saving it locally:
def getLines(filename):
    lines =  []
    
        # TutorialsPoint IDE requires 'r', not 'rb'
    #file = codecs.open(filename, encoding='utf-8')
    file = open(filename, 'r')
    for line in file:
      #print(line)
      lines.append(line)
    return lines


### FUNCTION TEXT2FREQ: Converts a text string or a list of strings into a frequency or count histogram
###                     This is essentially the Bag-of-Words (BoW) model
def text2freq(intext):
    # Make the string
    text = ""
    if isinstance(intext, str):   # Python 2: isinstance(arg, basestring)
        text = intext
    else:
        text = ' '.join(str(row) for row in intext)
    
    # Make the list of words with possible repeats
    words_list = [word.lower().strip(string.punctuation) for word in text.split()]
    #print(words_list)
    
    # CONVERT the LIST of words with possible repeats into a SET of unique words
    freq = {}
    words_set = set(words_list)
    for word in words_set:
        #freq[word] = words_list.count(word) / float(len(words_list))  # Frequency
        freq[word] = words_list.count(word)                            # Counts Only

    #print(sorted(freq))
    return freq

def pCC(user1, user2):
  sum_xy = 0
  sum_x = 0
  sum_y = 0
  sum_x2 = 0
  sum_y2 = 0
  n = 0

  #Compute Summation
  for eachKey in user1:
    if eachKey in user2:
      sum_xy += user1[eachKey]*user2[eachKey]
      sum_x += user1[eachKey]
      sum_y += user2[eachKey]
      sum_x2 += user1[eachKey]**2
      sum_y2 += user2[eachKey]**2
      n += 1

  if n == 0:
    return 0
  
  #Compute Numerator
  numerator = sum_xy - ((sum_x * sum_y)/n)
  
  #Compute Denominator
  denominator = (( sum_x2 -(((sum_x)**2)/n))*( sum_y2 -(((sum_y)**2)/n)))**(1/2)

  
  if denominator == 0:
    return 0

  else:
    return numerator/denominator

def cosineSimilarity(object1, object2):
  sum_xy = 0
  sum_x2 = 0
  sum_y2 = 0
  n = 0
  #Computations of summations
  for eachKey in object1:
    if eachKey in object2:
      sum_xy += object1[eachKey]*object2[eachKey]
      sum_x2 += object1[eachKey]**2
      sum_y2 += object2[eachKey]**2
      n += 1
  if n==0:
    return 0
  
  numerator = sum_xy
  denominator = ((sum_x2**(1/2)) * (sum_y2**(1/2)))
  if denominator == 0:
    print("Denominator is 0, no bueno!")
    return 0
  return numerator / denominator


### Check Test Cases:
text1 = ('Great Expectations', getLines('greatexpectations.txt'))
#text1 = ("I am a dog and I like to bark.")
freq1 = text2freq(text1)
#print(freq1)

text2 = ('Alice in Wonderland', getLines('alice.txt'))
#text2 = ("I am a dog and I like to bark.")
freq2 = text2freq(text2)
#print(freq2)
print('Comparison of', text1[0], 'to', text2[0], 'has cosine Similarity:', cosineSimilarity(freq1,freq2))
print('\tcosine Distance (the angle in radians):', math.acos(cosineSimilarity(freq1,freq2)))
print('\tand Pearson Correlation Coefficient:', pCC(freq1,freq2))




#Question 3

##These results are not as I had anticipated. Truthfully, I had expected a decent amount of similarity
##due to the nature of the English language, i.e. common terms such as 'a', 'the', etc. and their inherent
##frequency. What surprised me most was the severity that this measure had on impacting the results of our
##cosimilarity function. From a professional standpoint I would suggest that there is a high
##chance that these findings are highly skewed. A better alternative would be through utilization of
##something along the lines of context free grammars, or perhaps analyzing similar phrases as opposed to
##single words. Of course these would be more difficult to search for, and are not nearly as
##easy to put into being.



      
    
