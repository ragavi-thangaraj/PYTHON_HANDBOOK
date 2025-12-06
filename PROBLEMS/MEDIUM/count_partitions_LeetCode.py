# ------------------------------------------------------------
#  LeetCode Problem Solved : "Count Equal and Divisible Pairs in Array"
#  Problem Number : 3432
#
#  Logic:
#    - Maintain a left partition list 'li' and shrink the original list.
#    - After each split, compare the difference between sum(left) and sum(right).
#    - If the difference is even, increment the count.
#    - Continue until all valid partitions are checked.
#
#  Written by: Ragavi
#  Solved on: 05/12/2025
# ------------------------------------------------------------

class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        li = []

        # Create partitions by moving elements from nums to li
        while len(li) < n - 1:
            for i in nums:
                li.append(i)
                nums.remove(i)

                dif = sum(li) - sum(nums)

                # Check if difference is even
                if dif % 2 == 0:
                    count += 1
                else:
                    continue

        return count


# -------------------- User Input Section --------------------
# For local testing or pushing to GitHub

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements : ").split()))

    sol = Solution()
    result = sol.countPartitions(nums)
    print("Number of valid partitions:", result)

# -------------------- Sample Output Section --------------------
# Enter the array elements : 4 3 2 1
# Number of valid partitions: 2
