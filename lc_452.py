class Solution:
    def findMinArrowShots(self, points):
        points.sort(reverse = True)
        ans = 1
        curr_pos = points[0][0]
        for x, y in points:
            if y < curr_pos:
                curr_pos = x
                ans += 1
        return ans
