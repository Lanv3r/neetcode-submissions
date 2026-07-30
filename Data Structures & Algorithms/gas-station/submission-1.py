class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
            
        def greedy(i):
            tank = 0
            for k in range(n):
                j = (k + i) % n
                tank += gas[j] - cost[j]
                if tank < 0:
                    return False
            return True
        
        for i in range(n):
            if greedy(i):
                return i
