class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1

        i = 0
        tank = 0
        for j in range(n): 
            tank += (gas[j] - cost[j])
            if tank < 0:
                tank = 0
                i = j + 1
        return i
