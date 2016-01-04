def one():
    i=0
    j=0
    while (i<len(title)):
        if (quantity[j]>0):
            print("Title: %s , Author: %s , Amount of books available: %d , Price: %f" %(title[j], author[j], quantity[j], price[j]))
            j=j+1
        i=i+1
    return
        
def two(x):
    i=0
    flag=False
    while (i<len(title) and flag==False):
        if (x.lower()==title[i].lower()):
            print("Title: %s , Author: %s , Amount of books available: %d , Price: %f" %(title[i], author[i], quantity[i], price[i]))
            flag=True
        else:
           i=i+1
    if (flag==False):
        print("The book is not available")
    

def three(name):
    i=0
    flag=False
    while (i<len(author)):
        if (name.lower()==author[i].lower()):
            print("Title: %s , Author: %s , Amount of books available: %d , Price: %f" %(title[i], author[i], quantity[i], price[i]))
            flag=True
        i=i+1
            
    if (flag==False):
        print("There are no books available of this author")
    return

def four(x):
    i=0
    flag=False
    while (i<len(title) and flag==False):
        if (x.lower()==title[i].lower()):
            quantity[i]=quantity[i]-1
            flag=True
            return price[i]
        else:
           i=i+1
           
    


title = ["Ο άρχοντας των δαχτυλιδιών","Έγκλημα και τιμωρία","Η φάρμα των ζώων","Hobbit"]
author = ["J.R.R. Tolkien","Φ. Ντοστογιέφσκι","G.Orwell","J.R.R. Toklien"]
quantity = [5,2,4,1]
price = [11.4,13.7,9.7,8.5]
menu1 = ["1.","2.","3.","4.","5.","6.","7.","8."]
menu2 = ["See all Books available","Find a specific book","Find the books of a certain writer","Buy a book","Order a book","Change the price of a book","Display the amount of cash in the registry","Exit"]
registry = 0 #Bookshop's registry
i = 0
while (i < len(menu1)): #print of menu
    print (menu1[i], end=" ")
    print (menu2[i])
    print ()
    i = i+1

answer = int(input("Please choose one function: ")) #user's input
while (answer>8 or answer<1):
    print("Invalid input")
    answer = int(input("Please choose one function: "))

if (answer==1):
    one()
elif (answer==2):
    x = input("Please give me the title of the book: ")
    two(x)
elif (answer==3):
    name = input("Please give me the name of the author: ")
    three(name)
elif (answer==4):
    x = input("Give me the title of the book: ")
    z = four(x)
    registry = registry + z
    print(registry)
    print(quantity[3])
    
          
