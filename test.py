def one():
    i=0
    j=0
    while (i<len(title)):
        if (quantity[j]>0):
            print("Title: %s , Author: %s , Amount of books available: %d , Price: %f" %(title[j], author[j], quantity[j], price[j]))
        j=j+1
        i=i+1
    
        
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
    if (flag==False):
        print("There is no such book!")
        return 0
        
def five(x):
    i=0
    flag = False
    while (i<len(title) and flag==False):
        if (x.lower() == title[i].lower()):
            flag = True
            if (quantity[i]>=1):
                print("The book you want is available.")
                y = int(input("How many copies of this book do you want to buy: "))
                while (y > quantity[i]):
                    print("There are not so many copies available")
                    y = int(input("Please give me the number of copies you want to buy: "))
                quantity[i] = quantity[i] - y
                cash = y*price[i]
                return cash
            else:
                print("There are no copies available of the book you want!")
        i=i+1
        
    if (flag == False):
        print("This book does not exist in our bookstore!")
        title.append(x)
        a = input("Please give me the author of the book: ")
        author.append(a)
        b = int(input("Please give me the quantity of copies you want: "))
        quantity.append(b)
        c = float(input("Please give me the price of the book: "))
        price.append(c)
        if (b > 1):
            print("Your books have arrived! If you want to buy only one click on function 4. If you want to buy more than one click on function 5.")
            return 0
        else:
            print("Your book has arrived! If you want to buy it click on function 4.")

    
def six(x):
    i = 0
    flag = False
    while (i<len(title) and flag==False):
        if (x.lower() == title[i].lower()):
            flag = True
            price[i] = float(input("Please give me the new price of the book: "))
        i=i+1
    if (flag==False):
        print("There is no such book!")
    


title = ["Ο άρχοντας των δαχτυλιδιών","Έγκλημα και τιμωρία","Η φάρμα των ζώων","Hobbit"]
author = ["J.R.R. Tolkien","Φ. Ντοστογιέφσκι","G.Orwell","J.R.R. Toklien"]
quantity = [5,2,4,1]
price = [11.4,13.7,9.7,8.5]
menu1 = ["1.","2.","3.","4.","5.","6.","7.","8."]
menu2 = ["See all Books available","Find a specific book","Find the books of a certain writer","Buy a book","Order a book","Change the price of a book","Display the amount of cash in the registry","Exit"]
registry = 0.0 #Bookshop's registry
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

while ( answer!=8 ):

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
    elif (answer==5):
        x = input("Give me the title of the book: ")
        z = five(x)
        registry = registry + z
    elif (answer==6):
        x = input("Give me the title of the book: ")
        six(x)
    elif (answer==7):
        print(registry)
    print()
    i = 0
    while (i < len(menu1)): #print of menu again
        print (menu1[i], end=" ")
        print (menu2[i])
        print ()
        i = i+1
    answer=int(input("Please choose one function: "))
    print()
