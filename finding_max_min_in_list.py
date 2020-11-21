#  this is a basic python exercise: how to find the greatest or smallest number in a list without using python built in functions

list = [23, 0.81, 88.2, 18, -4.6, 71]

list_max = list[0]                                          #  let's suppose that the first element is the greatest, it might or might not be true
for i in range(len(list)):                                  #  let's go through the list one by one and examine if the particular element is greater than the first / previous element
    if list[i] > list_max:
        list_max = list[i]                                  #  if if the particular element is greater than any of the previous element then change it
print("The greats number in the list:\n", list_max, sep="")


list_min = list[0]                                          #  in this section everything happening similarly to to the previous one however it's applied to find the smallest number of the list
for i in range(len(list)):
    if list[i] < list_min:
        list_min = list[i]
print("The smallest number in the list:\n", list_min, sep="")
