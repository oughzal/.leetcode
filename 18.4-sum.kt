/*
 * @lc app=leetcode id=18 lang=kotlin
 *
 * [18] 4Sum
 */

// @lc code=start
class Solution {
    fun fourSum(nums: IntArray, target: Int): List<List<Int>> {
        nums.sort()
        val result = mutableListOf<List<Int>>()
        for (i in 0 until nums.size - 3) {
            if (i > 0 && nums[i] == nums[i - 1]) continue
            for (j in i + 1 until nums.size - 2) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue
            var left = j + 1
            var right = nums.size - 1
            while (left < right) {
                val sum = nums[i] + nums[j] + nums[left] + nums[right]
                when {
                sum == target -> {
                    result.add(listOf(nums[i], nums[j], nums[left], nums[right]))
                    while (left < right && nums[left] == nums[left + 1]) left++
                    while (left < right && nums[right] == nums[right - 1]) right--
                    left++
                    right--
                }
                sum < target -> left++
                else -> right--
                }
            }
            }
        }
        return result
    }
}
// @lc code=end

