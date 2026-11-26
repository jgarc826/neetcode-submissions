class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dictionart
        dictionary = {}
        
        # enumerate outputs the index and value of the list
        for index,val in enumerate(nums):
            # we will store the index of a value
            # key = value, value = index
            
            # the target - the value is difference
            # if difference is in the dictionary than we know the two
            # values that equal to twoSum
            difference = target - val
            if difference in dictionary:
                return [dictionary[difference],index]
            dictionary[val] = index
