'''
You are given an array of integer arr[] where each number represents a vote to a candidate. 
Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 
'''
# Python program to find Majority elements in an array
# using nested loops

def findMajority(arr):
    n = len(arr)
    res = []

    for i in range(n):
    
        cnt = 0
        for j in range(i, n):
            if arr[j] == arr[i]:
                cnt += 1
        
       
        if cnt > (n // 3):
            
          
            if len(res) == 0 or arr[i] != res[0]:
                res.append(arr[i])
        
      
        if len(res) == 2:
            if res[0] > res[1]:
                res[0], res[1] = res[1], res[0]
            break

    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")
