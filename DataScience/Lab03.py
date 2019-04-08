#Lab 03 | Mitchell Taylor | CSC 3005 | 6 March 2018 

#Problem #1
users={"Ricky":   {"Bob Seger":4.75,"CCR":4.5,"Beatles":5,"The Who":4.25,"Taylor Swift":4},
       "Meg":     {"Bob Seger":4,"CCR":3,"Beatles":5,"The Who":2,"Taylor Swift":1},
       "Mitch":     {"Bob Seger":4.8,"CCR":5,"Beatles":4.9,"The Who":4,"Taylor Swift":2},
       "Mary":     {"Bob Seger":3.5,"CCR":2,"Beatles":5,"The Who":5,"Taylor Swift":3},
       "Kristen":     {"Bob Seger":2,"CCR":5,"Beatles":1,"The Who":1,"Taylor Swift":4.5},
       "NullBoi": {"VeganFood":0}
       }

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

#Problem #2 
def recommendUser(user1, users):
  recList = []
  for eachUser in users:
    if user1 != eachUser:
      thresh = pCC(users[user1],users[eachUser])
      if thresh > 0:
        recList.append([eachUser,thresh,users[eachUser]])

  
  recList.sort(reverse=True)
  testList = recList[0][2]
  recommendations = []
  thresh = float(input("\nPlease enter a threshold value for your recommendations (0.0 through 1.0).\n"))
  print("\n")
  print("We recommend the following: ")
  for key, value in recList[0][2].items():
    if value > thresh:
      recommendations.append(key)

  return recommendations

print(recommendUser("Mitch", users))


##In order to implement a recommendation engine using PCC, we must see which PCC has the
##Highest value, then check individual ratings from the user with the highest PCC.
##Proceeding this we check if the values in this user are over a threshold, if they are
##print(recommend) them to the original user.


#Problem #3

##Provided that the PCC we found was +1, interpretation of theses results should be
##Very careful! While we can certaintly make a judgement call if our data set is massive enough,
##We must always be cautious when inferring anything. There could be external factors that could
##Bias our data/results, our deduction of this information (i.e. method of testing) might also
##Have flaws that we may not be immediately aware of. In terms of what I would tell a stake-
##-Holder; I would be excited to tell them that there may be a good bit of money to be made,
##As well as noting the unusually impressive results. I would make very clear that additional
##Methods of testing are recommended before making any big projects out of the conclusion of
##These tests. Should we find a consistant relationship between the two over multiple
##Experiments, then the assumption can be more trustworthy.
