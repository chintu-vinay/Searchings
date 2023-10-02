def binary_search(l1, lb, ub, sea_ele):
    if(lb > ub):
        return -1
    else:
        mid = (lb + ub) // 2
        if(l1[mid] == sea_ele):
            return mid
        elif(l1[mid] > sea_ele):
            return binary_search(l1, lb, mid - 1, sea_ele)
        else:
            return binary_search(l1, mid + 1, ub, sea_ele)
ran = int(input("Enter the range of numbers : "))
l1 = []
print("Enter the numbers : ")
for i in range(ran):
    l1.append(int(input()))
# Taking search element as input
sea_ele = int(input("Enter search element : "))
result = binary_search(l1, 0, ran - 1, sea_ele)
if(result != -1):
    print(f"Element found at index number {result}")
else:
    print("Element not found")