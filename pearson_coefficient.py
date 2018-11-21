  
for num in user1:
    if num in user2: 
      user1sum += user1[num]
      user2sum += user2[num]
      user1_times_user2 += user1[num] * user2[num]
      user1_squared += user1[num] ** 2
      user2_squared += user2[num] ** 2

    #there is no match among keys
    else: 
      return 0
      
  # algorithm nominator left side
  alg_nominator_pt1 = user1_times_user2

  # algorithm nominator right side
  alg_nominator_pt2 = (user1sum * user2sum) / len(user1)

  # algorithm denominator left side
  alg_denominator_pt1 = sqrt((user1_squared) - ((user1sum) ** 2)/len(user1))

  # algorithm denominator right side
  alg_denominator_pt2 = sqrt((user2_squared) - ((user2sum) ** 2)/len(user2))

  #algorithm nominator
  alg_nominator =  user1_times_user2 - ((user1sum * user2sum) / len(user1))

  #algorithm denominator
  alg_denominator = sqrt(user1_squared - ((user1sum ** 2) / len(user1))) * sqrt(user2_squared - ((user2sum ** 2) / len(user2)))
  
  return alg_nominator / alg_denominator


clara = {"Blues Traveler": 4.75, "Norah Jones": 4.5, "Phoenix": 5, "The Strokes": 4.25, "Weird Al": 4}
robert = {"Blues Traveler": 4, "Norah Jones": 3, "Phoenix": 5, "The Strokes": 2, "Weird Al": 1}

#function call
print(pearson(clara, robert))