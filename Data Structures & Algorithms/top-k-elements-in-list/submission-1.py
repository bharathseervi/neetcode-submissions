class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        result = []

        for i in range(k):
            maxFreq = 0
            maxNum = 0

            for num in count:
                if count[num] > maxFreq:
                    maxFreq = count[num]
                    maxNum = num

            result.append(maxNum)
            del count[maxNum]

        return result