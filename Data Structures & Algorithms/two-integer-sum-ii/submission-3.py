class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,val in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if val + numbers[j] == target:
                    return [i + 1, j + 1]