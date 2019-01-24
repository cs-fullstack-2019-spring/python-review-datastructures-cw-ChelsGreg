def main():
    # prob1()
    prob2()




# Create a function that has a loop that quits with q
# Allow the User to enter names until q is entered
# Add each name entered to a List
# When the User enters q print the list of names

#
#
# def prob1():
#
#     userList= input("Enter a name")
#     listNames = [userList]
#
#     while(userList.lower() != "q"):
#         userList = input("Enter another name")
#         listNames.append(userList)
#
#         if userList.lower() == "q":
#             break
#
#     print(listNames)
#







def prob2():


    myDictionList =  [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]



    for eachEl in myDictionList:
        print(f'Name: {eachEl["name"]} Age: {eachEl["age"]}')

    askUser = input("Do you want to sort by name or age?")

    while askUser != "q":
        askUser = input("What is the new sort criteria? Name or Age")
        if askUser == "age":
            myDictionList.sort("age")
            print(myDictionList)
        if askUser == "name":
            myDictionList.sort("name")
            print(myDictionList)
        else:
            break









































if __name__ == '__main__':
    main()