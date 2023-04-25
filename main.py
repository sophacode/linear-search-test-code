#linear search algorithm
def linearsearch(x):
  found = False
  index = 0
  searchItem = input("Enter the value you wish to search for: ")
  while not found and index < len(x):
    print (x[index])
    if x[index] == searchItem:
      found = True
    else:
      index = index + 1
  if found:
    print (searchItem, "was found at position", index)
  else:
    print ("Item not found")

#test data
nuumbers = ["1","2","3","4","5","6","7","8"]
linearsearch(nuumbers)