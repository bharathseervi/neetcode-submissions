class Solution:

    def quickSort(self, nums, low, high):

        while low < high:

            pivot = nums[low]

            i = low + 1
            j = high

            while i <= j:

                while i <= high and nums[i] <= pivot:
                    i += 1

                while j > low and nums[j] > pivot:
                    j -= 1

                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            # Put pivot in correct position
            nums[low], nums[j] = nums[j], nums[low]

            # Recursively sort smaller part
            if j - low < high - j:
                self.quickSort(nums, low, j - 1)
                low = j + 1
            else:
                self.quickSort(nums, j + 1, high)
                high = j - 1

    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums