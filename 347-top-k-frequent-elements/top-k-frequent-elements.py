class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # Step 1: Count frequency
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Create buckets
        # index = frequency
        bucket = [[] for i in range(len(nums) + 1)]

        # Step 3: Put each number in its frequency bucket
        for num in freq:
            count = freq[num]
            bucket[count].append(num)

        # Step 4: Start from highest frequency
        ans = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans   