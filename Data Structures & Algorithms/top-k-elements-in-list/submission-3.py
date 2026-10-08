class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}

        for i in range(len(nums)):
            if nums[i]in count:
                count[nums[i]]+=1
            else:
                count[nums[i]]=1
        

        sorted_list=sorted(count.items(), key=lambda x: x[1],reverse=True)

        ans=[]

        for i in range(k):
            ans.append(sorted_list[i][0])
        return ans
        