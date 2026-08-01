def calculate_love(name1, name2):
    names=name1.upper() + name2.upper()
    list=['T','R','U','E']
    list1=['L','O','V','E']
    true=0
    false=0

    for char in names:
        if char in list:
            true=true+1
    #print(true)
    for char1 in names:
        if char1 in list1:
            false+=1
    #print(false)

    print(f"Your love score is: {true}{false}%")


calculate_love("name1", "name2")