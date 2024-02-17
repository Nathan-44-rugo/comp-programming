#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        intersection_set = set(A) & set(B)
        count_a = 0
        count_b = 0
        for i in range(N):
            if A[i] in intersection_set and B.count(A[i]) == 1 :
                count_a+=1
            if B[i] in intersection_set and A.count(B[i]) == 1:
                count_b+=1
        if count_a == count_b:
            return True
        else:
            return False
        #return: True or False
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends
