#Function to remove all strings within a given list.
#E.g: [1, 2, 3 ,"Four", 5, "Six", "Seven", 8] should return [1, 2, 3, 5, 8]
def filter_list(list):
    resultList = []

    for item in list:
        if type(item) != str:
            resultList.append(item)

    return resultList

#The following function does the same as the above in a more concise way.
def filter_list_alt(l):
    return [x for x in l if type(x) is not str]

#Example demonstration.
givenList = [1, 2, 3 ,"Four", 5, "Six", "Seven", 8]
print(filter_list(givenList))
print(filter_list_alt(givenList))
