#217 Leetcode

class Solution(object):
  def containsDuplicate(self,nums):
    dup=set()
    for num in nums:
      if num in dup:
        return True
      dup.add(num)
    return False

Time complexity O(n)
space complexity O(1)
