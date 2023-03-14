class Solution(object):
    def threeSum(self,nums):
      # initialize an empty set to store the result
      result = set()
      # loop through the array from left to right
      for i in range(len(nums)):
        # use a dictionary to store the complements of the current number
        complements = {}
        # loop through the rest of the array
        for j in range(i + 1, len(nums)):
          # calculate the complement of nums[i] and nums[j] that sums to zero
          c = -(nums[i] + nums[j])
          # if the complement is already in the dictionary, add the triplet to the result
          if c in complements:
            result.add(tuple(sorted([nums[i], nums[j], c])))
          # else, add nums[j] to the dictionary as a key and its index as a value
          else:
            complements[nums[j]] = j
      output = []
      for elem in result:
        children = []
        for child in elem:
          children.append(child)
        output.append(children)


      return output