class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ri=-1
        for i in range(len(arr)-1,-1,-1):
            new=max(ri,arr[i])
            arr[i]=ri
            ri=new
        return arr