#integers=[]
odd=[]
even=[]
size=int(input("Enter the size of the list:: "))

for i in range(size):
    element=int(input(f"Enter the {i+1} integer: "))
    if element%2 == 0:
        even.append(element)

    else :
        odd.append(element)

    #integers.append(element)


print("The EVEN Elements of the List are:: ")
print(even)

print("The ODD Elements of the List are:: ")
print(odd)

