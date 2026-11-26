class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # value -> index
        dictionary = {}

        for index,number in enumerate(nums):
            if number in dictionary:
                return True
            else:
                dictionary[number] = index
        
        return False
