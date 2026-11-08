class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1 = cand2 = None
        count1 = count2 = 0

        # Find 2 possible candidates
        for num in nums:
            if num == cand1:
                count1 += 1

            elif num == cand2:
                count2 += 1

            elif count1 == 0:
                cand1 = num
                count1 = 1

            elif count2 == 0:
                cand2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates
        result = []

        if nums.count(cand1) > len(nums) // 3:
            result.append(cand1)

        if nums.count(cand2) > len(nums) // 3:
            result.append(cand2)

        return result    