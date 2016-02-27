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
Menu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Interests = [] 
temp = []
temp1 = []

i=1
for k in General:
    print (repr(i) + "." + repr(k))
    i = i + 1

for key in General:
    temp.append(key)

print(temp)
    
k=0
z=-1
flag1=False
while (k<20 and flag1==False):
    flag = False
    answer = input("Choose your interests : ")
    while ((i<len(temp)) and (flag1==False)):
        z = z + 1
        if (answer.lower()=='Escape'):
            flag1=True
        if (answer.lower()==temp[i]):
            Interests[k] = i
            k = k + 1
    k = k + 1

k=0
while (k<len(Interests)):
    print(Interests[k])
