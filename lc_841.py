"""
  Leetcode #841
  https://leetcode.com/problems/keys-and-rooms/
"""

class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)
        visited[0] = True

        def dfs(k):
            for room in rooms[k]:
                if not visited[room]:
                    visited[room] = True
                    dfs(room)
        
        dfs(0)
        return all(visited)
