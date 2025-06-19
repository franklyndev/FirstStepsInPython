
num = [5, 6, 4, 3, 7, 9]
print(num,"| Normal")
num.append(1) # Add some element at the end in List
print(num,"| Added 1")
print(f"This List has {len(num)} elements") # The Length of the List, how many elements it has
num.sort() # To sort elements in List
print(num,"| Sorted")
num.sort(reverse=True) # To reverse the elements of one List
print(num,"| Reversed")
num.insert(3, 10) # Add an element at specific spot of one List
print(num, "Added at the position 3, element 10 ")
del (num[3]) # Remove an element at specific spot 
print(num)
num.pop() # Remove an element at the end, u can also remove at specific spot by selecting a spot in the brackets   
print(num)

val = []
val.append(5)
val.append(6)
val.append(7)
for c, v in enumerate(val):
    print(f"position {c} = {v}")
