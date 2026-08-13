set1 = {1,2,3,4,5,6,7,8,9,10}
print("Your Set is: ", set1)
list1 = [{1,2}, {11,16}, {8,10}, {25,56}]
print("Your list1 is: ", list1)

common1 = [i for i in list1 if i.isdisjoint(set1)]
print("Not in your Set: ", common1)
