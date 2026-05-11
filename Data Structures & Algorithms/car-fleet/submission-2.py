class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = [0]
        cars = {}

        for i in range(len(position)):
            cars[position[i]] = speed[i]

        position = sorted(position)[::-1]

        for i in range(len(position)):
            time = (target - position[i]) / cars.get(position[i]) 
            if time > fleets[0]:
                fleets = [time] + fleets

            
        return len(fleets)-1

