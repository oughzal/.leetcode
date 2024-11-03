/*
 * @lc app=leetcode id=680 lang=kotlin
 *
 * [680] Valid Palindrome II
 */

// @lc code=start
class Solution {
    private fun isPalindrome(s: String, i: Int, j: Int): Boolean {
    var start = i
    var end = j
    while (start < end) {
        if (s[start] != s[end]) {
            return false
        }
        start++
        end--
    }
    return true
    }
    
    fun validPalindrome(s: String): Boolean {
        var i = 0
        var j = s.length - 1
        while (i < j) {
            if (s[i] != s[j]) {
                return isPalindrome(s, i + 1, j) || isPalindrome(s, i, j - 1)

            }
            i++
            j--
        }
        return true
        
    }
}
// @lc code=end

