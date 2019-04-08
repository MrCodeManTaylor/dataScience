# Mitchell Taylor  |  LAB 06
#

from math import sqrt


# Extended Dataset:
users = {"Jackie": {  "CCR": 3,
                        "Beatles": 5,
                        "Taylor Swift": 4,
                        "Rebecca Black": 1},

         "Johnny":{    "CCR": 3,
                        "Beatles": 4,
                        "Taylor Swift": 4,
                        "Rebecca Black": 1},

         "Ricky": {    "Bob Seger": 4,
                        "CCR": 3,
                        "Taylor Swift": 3,
                        "Rebecca Black": 1},

         "Megan": {   "Bob Seger": 4,
                        "CCR": 4,
                        "Beatles": 4,
                        "Taylor Swift": 3,
                        "Rebecca Black": 1},

         "Cindy": {    "Bob Seger": 5,
                        "CCR": 4,
                        "Beatles": 5,
                        "Rebecca Black": 3}
        }

# Adjusted Cosine Similarity
def cACS(band1, band2):
    # Build our averages
    averages = {}
    for (key, ratings) in users.items():
      averages[key] = (float(sum(ratings.values())) / len(ratings.values()))
    # Compute the actual similarity
    num  = 0  # numerator
    den1 = 0  # first half of denominator
    den2 = 0
    for key in users:
      if band1 in users[key]:
          if band2 in users[key]:
            num += (users[key][band1] - averages[key] ) * (users[key][band2] - averages[key])
            den1 += (users[key][band1] - averages[key] )**2
            den2 += (users[key][band2] - averages[key] )**2
            
    # First, compute the normalized rating for each band (band1 and band2)
    return round((num / (sqrt(den1) * sqrt(den2))),4)



def populatematrix(dataSet):
    bandList = []
    similarityMatrix = []
    for key in dataSet:
      for band in dataSet[key]:
          if band not in bandList:
              bandList.append(band)
              
    similarityMatrix = {}
    simMat = []
    for band in bandList:
      for nextBand in bandList:           
          similarityMatrix[nextBand] = cACS(band, nextBand)
      simMat.append((band,similarityMatrix.copy()))
    return simMat
  
a = populatematrix(users)
print(a)              #Do this to print out the whole matrix
print(a[0][1]['CCR']) #Do this to print out a specific value (i.e. CCR compared with CCR)


#REJOICE. 


