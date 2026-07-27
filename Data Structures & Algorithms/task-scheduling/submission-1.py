class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        cooldown = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        cycles = 0
        while freq:
            sorted_list = sorted(freq.items(), key=lambda item: item[1], reverse=True)
            for i in range(len(sorted_list)):
                t = sorted_list[i][0]
                if cooldown.get(t, 0) <= 0: 
                    freq[t] -= 1
                    cooldown[t] = n + 1
                    if freq[t] == 0:
                        del freq[t]
                    break
            cycles += 1
            for k in cooldown:
                cooldown[k] -= 1

        return cycles
