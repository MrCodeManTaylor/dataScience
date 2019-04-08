#Lab 05 | Mitchell Taylor | 4.12.2018

# kNN implementation in Python 3

import csv
import random
import math
import operator
import urllib.request

# Old Way Commented-Out



### FUNCTION GET LINES: Get the files, either directly online or by saving it locally:
def getLines(filename):
    lines =  []
    if (filename.startswith(('http', 'ftp', 'sftp')) ):
        # Skip downloading it and open directly online:
        response = urllib.request.urlopen(filename)
        lines = csv.reader(response.read().decode('utf-8').splitlines())
    else:
        # TutorialsPoint IDE requires 'r', not 'rb'
        with open(filename, 'r') as csvfile:
            # csvreader is an object that is essentially a list of lists
            csvreader = csv.reader(csvfile)
            for line in csvreader:
                lines.append(line)
    return lines

def loadDatasetFinal(filename, split, trainingSet=[] , testSet=[]):
    lines = getLines(filename)
    #for row in lines:
    #    print (', '.join(row))

    dataset = list(lines)
    for x in range(len(dataset)-1):
        for y in range(4):                        # legend = ('Sepal length', 'Sepal width', 'Petal length', 'Petal width')
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)
def cosineSimilarity(object1, object2,length):
  sum_xy = 0
  sum_x2 = 0
  sum_y2 = 0
  n = 0
  #Computations of summations
  for x in range(length):
    if x in object2:
      sum_xy += object1[x]*object2[x]
      sum_x2 += object1[x]**2
      sum_y2 += object2[x]**2
      n += 1
  if n==0:
    return 0
  
  numerator = sum_xy
  denominator = ((sum_x2**(1/2)) * (sum_y2**(1/2)))
  if denominator == 0:
    print("Denominator is 0, no bueno!")
    return 0
  return numerator / denominator
def pCC(user1, user2, length):
  sum_xy = 0
  sum_x = 0
  sum_y = 0
  sum_x2 = 0
  sum_y2 = 0
  n = 0

  #Compute Summation
  for eachKey in range(length):
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

def minkowskiDistance(ratingsUser1, ratingsUser2,length):
  distance = 0
  p = 0
  for key in range(length):
    if key in ratingsUser2:
      p = p+1
  for key in range(length):
    if key in ratingsUser2:
      distance += (abs((ratingsUser1[key] - ratingsUser2[key])))**p
  if p == 0:
    distance = distance**(1)
  else:
    distance = distance**(1/p)
  distance = round(distance, 3)
  return distance

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
  
def getNeighborsCOS(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = cosineSimilarity(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
  
def getNeighborsPCC(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = pCC(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getNeighborsMINKOWSKI(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = minkowskiDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
  
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
  
def wrappedAverage(n):
  # prepare data
    k = int(input("How many neighbors would you like to compute?\n"))
    uVal =int(input("Enter: \n1 for Euclidean\n2 for Minkowski \n3 for Pearson \n4 for Cosine Similarity\n")) 
    wrappedAvg = 0
    avgTrainingSet = 0
    avgTestSet = 0
    split = 0.67
    filename = 'iris.data'
    for x in range(n):
      trainingSet=[]
      testSet=[]
      print("\nTrial: ", x+1, "\n")
      loadDatasetFinal(filename, split, trainingSet, testSet)
      print('Train set: ' + repr(len(trainingSet)))
      print('Test set: ' + repr(len(testSet)))
      avgTrainingSet += len(trainingSet)
      avgTestSet += len(testSet)


      # generate predictions
      predictions=[]
      for x in range(len(testSet)):
          if uVal == 1:
            neighbors = getNeighbors(trainingSet, testSet[x], k)
          elif uVal == 2:
            neighbors = getNeighborsMINKOWSKI(trainingSet, testSet[x], k)
          elif uVal == 3:
            neighbors = getNeighborsPCC(trainingSet, testSet[x], k)
          elif uVal == 4:
            neighbors = getNeighborsCOS(trainingSet, testSet[x], k)
          else:
            neighbors = getNeighbors(trainingSet, testSet[x], k)  
          result = getResponse(neighbors)
          predictions.append(result)
          #print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
      accuracy = getAccuracy(testSet, predictions)
      print('\n> Accuracy: ' + repr(accuracy) + '%')

      wrappedAvg += accuracy
      print("\n")
    wrappedAvg =  wrappedAvg / n
    print("\n>Average Accuracy:  ",wrappedAvg,"\n")
    avgTestSet = avgTestSet / n
    avgTrainingSet = avgTrainingSet / n

    return wrappedAvg
  
def main():
    # set our parameters
    n = int(input("How many tests would you like to run for your accuracy?\n"))
    print("\n")
    print("Your average accuracy is: ", wrappedAverage(n), "%\n")
    

main()

### Number 1:
##On separate tests values of accuracy change; this is due to the way in which we define
##and break up our test set and training set. These numbers tend to change on a case-to-case
##basis; this is most likely due to the computers method of defining 1/3 and 2/3's of a whole
##number. 





