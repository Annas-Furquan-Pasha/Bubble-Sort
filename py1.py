#Bubble sort

arr = [1,2,3,5,4,6]
swap = False

for i in range(0, len(arr)-1):
  for j in range(0, len(arr)-i-1):
    if arr[j] > arr[j+1]:
      swap = True
      arr[j], arr[j+1] = arr[j+1], arr[j]

  if not swap:
    break

print('The sorted array is : ') if swap else print('The array is already sorted')
for i in arr:
  print(i, end=" ")