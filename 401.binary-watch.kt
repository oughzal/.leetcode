/*
 * @lc app=leetcode id=401 lang=kotlin
 *
 * [401] Binary Watch
 */

// @lc code=start
class Solution {
    fun readBinaryWatch(turnedOn: Int): List<String> {
        val res = mutableListOf<String>()
        for (i in 0 until 12) {
            for (j in 0 until 60) {
                if (Integer.bitCount(i) + Integer.bitCount(j) == turnedOn) {
                    res.add("$i:${if (j < 10) "0$j" else j}")
                }
            }
        }
        return res
        
    }
}
// @lc code=end

