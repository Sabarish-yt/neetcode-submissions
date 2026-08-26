from typing import List


class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    res = 0
    store = set(nums)

    for num in store:
      # ONLY start counting if 'num' is the beginning of a sequence
      if (num - 1) not in store:
        streak, curr = 0, num
        while curr in store:
          streak += 1
          curr += 1
        res = max(res, streak)

    return res