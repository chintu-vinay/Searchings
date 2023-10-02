ran = int(input("Enter the range of numbers : "))
l1 = []
# Initilizing search element found value as 0
found = 0
print("Enter the numbers : ")
for i in range(ran):
    l1.append(int(input()))
# Taking search element as input
sea_ele = int(input("Enter search element : "))
for i in range(ran):
    if(sea_ele == l1[i]):
        found += 1
        break
if(found == 1):
    print(f"Search element found at index number {i}")
else:
    print("Search element is not present in given list")
