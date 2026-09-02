class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        c=0
        stack=[]

        for i,h in enumerate(heights):
            st=i
            while stack and stack[-1][1]>h:
                ind,hi=stack.pop()
                c=max(c,hi * (i - ind))
                st=ind
            stack.append((st,h))

        for i, h in stack:
            c=max(c, h * (len(heights) - i))
        return c            