print("Average calculator (Version 1.0)\nDeveloped by Sebastián Ramírez")
prompt = (input("Type *file* for opening a file with grades to calculate the your average, *fast* to enter the grades manually or *quit* for exit the program: "))

#File calculation code
if prompt == "file" :
    fname = input("Enter the file with grades: ")
    fhandle = open(fname)
    for line in fhandle :
        grades = list()
        line = line.strip()
        tmp = line.split(",")
        tmpGrades = tmp[1:]
        for thing in tmpGrades :
            thing = int(thing)
            grades.append(thing)
        print(tmp[0], sum(grades) / len(grades))

#Fast calculation code
elif prompt == "fast" :
    getGrades = None
    grades = list()
    while getGrades != "done" :
        getGrades = input("Write your grade, write *done* when ready: ")
        if getGrades != "done" :
            try :
                getGrades = int(getGrades)
                if getGrades <= 20 and getGrades > 1 :
                    grades.append(getGrades)
                else :
                    print("Input is out the parameter")
            except :
                print("Invalid input")
                continue
    if len(grades) > 0 :
        print("Your average is", sum(grades) / len(grades))

#Program exit code
elif prompt == "quit" :
    quit()

#Invalid input code
else :
    print("Please run the program again and enter a valid input")
