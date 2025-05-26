'''
You are given an array of integer arr[] where each number represents a vote to a candidate. 
Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 
'''
def findMajority(arr):
  n = len(arr)

ele1, ele2 = -1, -1
cnt1, cnt2 = 0, 0

for r
