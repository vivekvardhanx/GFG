'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
'''
def getSecondlargest(self,arr)
n = len(arr)
if n<2:
  return -1
first = second = float('-inf')
for num in arr
    if num = first:
       second = first
       first = num  
    elif num > second and num != first:
       second = num
 if second == float('arr')
    return -1
 else:
  return second
