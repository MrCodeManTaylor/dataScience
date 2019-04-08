# Data Science | Dr. Sethi | 02.20.2018
# Lab 02 | Mitchell Taylor

#Initial Data Set


# Problem
users={
      "Andy": {"Hawking":5,"Feynman":5,"Bryson":1},
      "Bob": {"Hawking":5,"Feynman":2,"Bryson":4},
      "Johnny": {"Hawking":4,"Feynman":1,"Bryson":5,},
      "Mr.X": {"Hawking":2,"Feynman":4},
      "Gertrude": {"Hawking":1,"Feynman":1,"Bryson":5},
      "Herman": {"Hawking":1,"Feynman":3,"Bryson":5},
      "Nicolas": {"Hawking":2,"Feynman":5,"Bryson":2,"Dr.Seuss":3},
      "Zarya": {"Hawking":3,"Feynman":4},
      "Devon": {"Hawking":3,"Feynman":1,"Dr.Seuss":3},
      "Swan": {"Hawking":5,"Bryson":2}
      }

#Manhattan Distance Metric
def manhattanDistance(ratingsUser1, ratingsUser2):
  distance = 0
  for key in ratingsUser1:
    if key in ratingsUser2:
      distance += abs(ratingsUser1[key] - ratingsUser2[key])
  if distance != 0:
    return distance
  else:
    return 0
    

#Euclidean Distance Metric
def euclideanDistance(ratingsUser1, ratingsUser2):
  distance = 0
  for key in ratingsUser1:
    if key in ratingsUser2:
      distance += ((ratingsUser1[key] - ratingsUser2[key])**2)
  distance = round((distance**(1/2)),3)
  return distance

#Minkowski Distance Metic
def minkowskiDistance(ratingsUser1, ratingsUser2):
  distance = 0
  p = 0
  for key in ratingsUser1:
    if key in ratingsUser2:
      p = p+1
  for key in ratingsUser1:
    if key in ratingsUser2:
      distance += (abs((ratingsUser1[key] - ratingsUser2[key])))**p
  if p == 0:
    distance = distance**(1)
  else:
    distance = distance**(1/p)
  distance = round(distance, 3)
  return distance

#Asked for version of nearest neighbor
def computeNearestNeighbor(username, users):
  distances = []
  userslist = []
  i = 0
  for username in users:
    userslist.append(username)
  for username in users:
    distances.append([minkowskiDistance(users[username], users[userslist[i]]),username])
  distances.sort()
  print(distances)

#Personal version of nearest neighbor
def computeNearestNeighborV2(username1, users):
  distancesM = []
  distancesE = []
  distancesMH = []
  userslist = []
  i = 0
  for username in users:
    userslist.append(username)
  print("Mankowski Distances. \n")
  for username in users:
    distancesM.append([username1, minkowskiDistance(users[username1], users[userslist[i]]), userslist[i]])
    i += 1
  distancesM.sort()
  a = 0
  for instances in users:
    print(distancesM[a],"\n")
    a +=1
  i = 0
  print("Euclidean Distances. \n")
  for username in users:
    distancesE.append([username1, euclideanDistance(users[username1], users[userslist[i]]), userslist[i]])
    i += 1
  distancesE.sort()
  a = 0
  for instances in users:
    print(distancesE[a],"\n")
    a += 1
  
  i = 0
  print("Manhattan Distances. \n")
  for username in users:
    distancesMH.append([username1, manhattanDistance(users[username1], users[userslist[i]]), userslist[i]])
    i += 1
  distancesMH.sort()
  a = 0
  for instances in users:
    print(distancesMH[a],"\n")
    a += 1

#Calling functions

#print("Manhattan Distance from Andy to Mr.X", manhattanDistance(users["Andy"], users["Mr.X"]))
#print("Euclidean Distance from Andy to Mr.X", euclideanDistance(users["Andy"], users["Mr.X"]))
#print("Minkowski Distance from Andy to Mr.X", minkowskiDistance(users["Andy"], users["Mr.X"]))

def computeNearestNeighborV3(users):
  distancesM = []
  distancesE = []
  distancesMH = []
  userslist = []
  j = 0
  totalUsers = 0
  for username in users:
    userslist.append(username)
    totalUsers += 1
  print("Minkowski Distances. \n")
  for username in users:
    i=0
    username = userslist[j]
    for eachUser in users:
      testval = minkowskiDistance(users[username], users[userslist[i]])
      if testval != 0:
        distancesM.append([username, minkowskiDistance(users[username], users[userslist[i]]), userslist[i]])
      i += 1
    j += 1
  distancesM.sort()
  print("\nNow printing MINKOWSKI DISTANCES for each user in the userlist. \n")
  a = 0
  for eachInstance in distancesM:
    print(distancesM[a])
    a +=1
  print("\nNow printing MSU for each user in the userlist. \n")
  b = 0
  c = 0
  for eachInstance in distancesM:
    while c <= totalUsers-1 :
      print(distancesM[b])
      b += totalUsers -1
      c += 1
  
  print("\n \n")
  print("Euclidean Distances. \n")
  j = 0
  for username in users:
    i=0
    username = userslist[j]
    for eachUser in users:
      testval = euclideanDistance(users[username], users[userslist[i]])
      if testval != 0:
        distancesE.append([username, euclideanDistance(users[username], users[userslist[i]]), userslist[i]])
      i += 1
    j += 1
  distancesE.sort()
  print("\nNow printing EUCLIDEAN DISTANCES for each user in the userlist. \n")
  a = 0
  for eachInstance in distancesE:
    print(distancesE[a])
    a +=1
  print("\nNow printing MSU for each user in the userlist. \n")
  b = 0
  c = 0
  for eachInstance in distancesE:
    while c <= totalUsers-1 :
      print(distancesE[b])
      b += totalUsers -1
      c += 1
  
  print("\n \n")
  print("Manhattan Distances. \n")
  j = 0
  for username in users:
    i=0
    username = userslist[j]
    for eachUser in users:
      testval = manhattanDistance(users[username], users[userslist[i]])
      if testval != 0:
        distancesMH.append([username, manhattanDistance(users[username], users[userslist[i]]), userslist[i]])
      i += 1
    j += 1
  distancesMH.sort()
  print("\nNow printing MANHATTAN DISTANCES for each user in the userlist. \n")
  a = 0
  for eachInstance in distancesMH:
    print(distancesMH[a])
    a +=1

  print("\nNow printing MSU for each user in the userlist. \n")
  b = 0
  c = 0
  for eachInstance in distancesMH:
    while c <= totalUsers-1 :
      print(distancesMH[b])
      b += totalUsers -1
      c += 1
  
#Most optimal version of nearestNeighbor | Outputs nearest neighbor to each instanced user is list, EXCLUDES 0 DISTANCE MEASURES
def nearestNeighbor(users):
  print("\nNearest Neighbor OPTIMAL \n")
  distancesM = []
  userslist = []
  j = 0
  totalUsers = 0
  for username in users:
    userslist.append(username)
    totalUsers += 1
  for username in users:
    i=0
    username = userslist[j]
    for eachUser in users:
      testval = username
      if testval != userslist[i]:
        distancesM.append([username, minkowskiDistance(users[username], users[userslist[i]]), userslist[i]])
      i += 1
    j += 1
  distancesM.sort()
  print("\nNow printing MSU for each user in the userlist via Minkowski Distance. \n")
  b = 0
  c = 0
  for eachInstance in distancesM:
    while c <= totalUsers-1 :
      print(distancesM[b])
      b += totalUsers -1
      c += 1

#print("Nearest Neighbor VOriginal")
#computeNearestNeighbor("Andy",users)
#print("Nearest Neighbor V2")
#computeNearestNeighborV2("Andy",users)
#print("Nearest Neighbor V3")
#computeNearestNeighborV3(users)
nearestNeighbor(users)

# 3
#
#Defining distance metrics
#
# A distance metric is the definition of the non-negative distance between elements of a set.
# This differs from a measurement, which is derived through the distance between points. A metric is the measure of the differences
# Between these measures.
# A measure of measures, so to speak.
#
#Source: https://numerics.mathdotnet.com/distance.html
