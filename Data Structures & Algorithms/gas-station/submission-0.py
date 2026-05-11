class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        def simulate_circuit(start, gas, cost):
            i = start
            flag = True
            tank = 0

            while i != start or flag:
                tank += (gas[i] - cost[i])

                if tank < 0:
                    return False

                i = (i+1) % len(gas)
                flag = False

            return True


        for i in range(len(gas)):
            if simulate_circuit(i, gas, cost):
                return i
        return -1
            
