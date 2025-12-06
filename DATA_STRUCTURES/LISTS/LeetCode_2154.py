# ------------------------------------------------------------
#  LeetCode Problem Solved : "Keep Multiplying Found Values by Two"
#  Problem Number : 2154
#
#  Logic:
#    - Check if 'original' exists in nums.
#    - If yes → multiply it by 2.
#    - Keep repeating until 'original' is NOT found.
#
#  Written by: Ragavi
#  Solved on: 06/12/2025
# ------------------------------------------------------------

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        
        # Continue multiplying while original is found in the list
        while original in nums:
            original *= 2

        return original


# -------------------- User Input Section --------------------
# This section is just for running locally or pushing to GitHub.

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements : ").split()))
    original = int(input("Enter the original number: "))

    sol = Solution()
    result = sol.findFinalValue(nums, original)
    print("Final value after process:", result)

# -------------------- Sample Output Section --------------------   
# Enter the array elements : 5 3 6 1 12
# Enter the original number: 3
# Final value after process: 24
