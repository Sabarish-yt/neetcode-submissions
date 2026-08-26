class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0] * n
        for i in range(n-1):
            ans[i]=max(arr[i+1:n])
        ans[n-1]=-1    
        return ans    
