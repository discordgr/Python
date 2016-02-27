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
         'Exit' : None
                 }
Menu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
Interests = [] 


i=1
for k in sorted(General):
    print (repr(i) + "." + repr(k))
    i = i + 1

k=0
z=-1
flag1=False
while (k<20 and flag1==False):
    flag = False
    answer = input("Choose your interests : ")
    for i in General.items():
        z = z + 1
        if (answer.lower()=='Exit'):
            flag1=True
        if (answer.lower()==i):
            Interests[k] = i
            k = k + 1
            General[i] = True
        else:
            if ((flag==False) and (z==19)):
                print("Possibly wrong answer")
                print("Try again")
                flag=True
    k = k + 1

k=0
while (k<len(Interests)):
    print(Interests[k])
