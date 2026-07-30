class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1

        i = 0
        while i < n:
            tank = 0
            for j in range(n): 
                k = (i + j) % n
                tank += gas[k] - cost[k]
                if tank < 0:
                    i = k + 1
                    break
            if tank >= 0:
                return i
