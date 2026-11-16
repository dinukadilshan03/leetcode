class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uniques = set()
        for selected in nums:
            if selected in uniques:
                return True
            if selected not in uniques:
                uniques.add(selected)
            
        
        return False


            

                

        