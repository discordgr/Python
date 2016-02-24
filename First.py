Movies = ["Action", "Drama", "Comedy", "Fantasy", "Adventure","Exit"]
Books = ["Action", "Drama", "Comedy", "Fantasy", "Adventure","Exit"]
VideoGames = ["Action", "RPG", "MMO", "Simulation", "Strategy","Exit"]
Menu = [1,2,3,4,5,6]
User = {'Movies' : 0, 'Books' : 0, 'VideoGames' : 0}
UserGen = []
temp1 = []
temp2 = []

k=0
while (k < len(Movies)):
    temp1.append(Movies[k]);    
    k = k + 1
k=0
while (k < len(Menu)):
    temp2.append(Menu[k]);
    k = k + 1

i = 0
while (i < len(Movies)):
    if (i == 0):
        print ("What Genre do you prefer? ")
    print (Menu[i], end=" ")
    print (Movies[i])
    i = i + 1
    
answer = int(input("Please choose one of the above : "))
while (answer>6 or answer<1):
    print("Invalid input")
    answer = int(input("Please choose one of the above : "))

j=6
while ( answer!=j ):

    if (answer==1):
        User['Movies'] = User['Movies'] + 5
        UserGen.append(Movies[0]);
        temp1.remove(Movies[0]);
    elif (answer==2):
        User['Movies'] = User['Movies'] + 5
        UserGen.append(Movies[1]);
        temp1.remove(Movies[1]);
    elif (answer==3):
        User['Movies'] = User['Movies'] + 5
        UserGen.append(Movies[2]);
        temp1.remove(Movies[2]);
    elif (answer==4):
        User['Movies'] = User['Movies'] + 5
        UserGen.append(Movies[3]);
        temp1.remove(Movies[3]);
    elif (answer==5):
        User['Movies'] = User['Movies'] + 5
        UserGen.append(Movies[4]);
        temp1.remove(Movies[4]);
        
    temp2.remove(j);
    j = j - 1
    print()
    print("Do you want to choose another genre?")
    print("1. Yes")
    print("2. No")
    answer1 = int(input("Please choose one of the above : "))
    print()
    
    if (answer1==1):
        i = 0
        while (i < len(temp1)):
            if (i == 0):
                print ("What Genre do you prefer? ")
            print (temp2[i], end=" ")
            print (temp1[i])
            i = i + 1

        answer = int(input("Please choose one of the above : "))
        while (answer>j or answer<1):
            print("Invalid input")
            answer = int(input("Please choose one of the above : "))
    else:
        answer=j

print(User['Movies'])
  
    
