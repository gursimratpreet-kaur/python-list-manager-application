#Author:Gursimratpreet Kaur
#Student ID:991845418
#Assignment-2 Program-3


#https://realpython.com/python-split-string/#how-to-split-a-string-in-python-using-split

strings=input("Enter the strings separated by space: ")
List=strings.split()
#print(List)


#To tell users how many strings they have entered
print(f"{len(List)} strings have been entered.")

#Menu Options
#Clear list2. Print list 3. Alphabetize list 4. Add word(s) to list 5. Delete word(s) from list 6. Remove duplicate words from list 7. Exit program 
print("Menu Options are:")
menuOpt=["1. Clear List","2. Print List","3. Alphabetize list","4. Add word(s) to list", "5. Delete word(s) from list","6. Remove duplicate words from list","7. Exit program "]
count=0
while True:
    for option in menuOpt:
        print(option)
    userOpt=input("Make a choice: ")
    if userOpt=="7":
        a=input("Are you sure?(yes/no)")
        if a=="yes": 
            print("Done")
            break
    elif userOpt=="3":
        #List.sort()
        List.sort()
        print(List)   
    elif userOpt=="4":
        itemlist=input("Enter word(s) to be added: ").split()
        c=input("Do you want to add items in alphabetized list?(yes/no)")
        if c=="yes":
            for i in itemlist:  #To add more than one word separated by space character
                List.append(i)
                List.sort()
            print(List)
        elif c=="no":
            for n in itemlist:
                List.append(n)
            print(List)
        d=input("Do you want to add more words?(yes/no)")
        if d=="yes":
            itemlist=input("Enter word(s) to be added: ").split()
            c=input("Do you want to add items in alphabetized list?(yes/no)")
            if c=="yes":
                for i in itemlist:  #To add more than one word separated by space character
                    List.append(i)
                    List.sort()
                print(List)
            elif c=="no":
                for n in itemlist:
                    List.append(n)
                print(List)
        
    elif userOpt=="5":
        delItem=input("Enter word(s) to be deleted: ").split()
        for j in delItem:
            List.remove(j)
            count+=1
            removedItem=j
        print(f"{count} word(s) have been removed")
        info=input("Do you need more information?(yes/no)")
        if info=="yes":
            print(f"words removed are:{removedItem}")
        print(List)
    elif userOpt=="2":
        print(f"The list is :{List}")
    
    elif userOpt=="6":
        a=input("Are you sure?(yes/no)")
        if a=="yes":
            for k in List:
                if List.count(k)>=2:
                    List.remove(k)
            print(List)
    elif userOpt=="1":
        a=input("Are you sure?(yes/no)")
        if a=="yes":
            List[:]=[]
            print(List)
            
                
         
