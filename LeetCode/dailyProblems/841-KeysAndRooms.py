class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # initialize values
        n = len(rooms)
        visited = set()
        keys = [] # better to use set?

        # visit room 0
        visited.add(0)
        for i in range(len(rooms[0])):
            if (rooms[0][i] not in visited):
                keys.append(rooms[0][i])
        
        # repeat
        while (keys != []):

            # get a key
            curr = keys.pop()

            # visit room curr
            visited.add(curr)
            for i in range(len(rooms[curr])):
                if (rooms[curr][i] not in visited):
                    keys.append(rooms[curr][i])
        
        # return
        return (n == len(visited))
