General =       {
         'Sports and Fitness' : None,
	 'Movies' : None,
	 'VideoGames' : None,
	 'College Studies' : None,
	 'Books' : None,
	 'Music' : None,
	 'Internet' : None,
	 'TV' : None,
	 'Computers' : None,
	 'Animals' : None,
	 'Arts' : None,
	 'Cars' : None,
	 'Anime' : None,
	 'Nature' : None,
	 'Nightlife' : None,
	 'Photography' : None,
	 'Travel' : None,
	 'Social Media' : None,
	 'House Activities' : None,
         'Escape' : None
                 }

Interests = [] 
temp = []


i=1
for k in General:
    print (repr(i) + "." + repr(k))
    i = i + 1

for key in General:
    temp.append(key)

#print(temp)

i=0
while (i<len(temp)):    
    k = 0
    answer = input("Choose your interests : ")
    while (k < len(temp)):
        if (answer == temp[k]):
            Interests[i] = temp[k]
        else:
            k = k + 1
    i=i+1
print(Interests)    


