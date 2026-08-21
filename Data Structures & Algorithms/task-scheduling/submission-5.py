class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {} 
        k, top_task = 0, None  # Most frequent task.
        
        for task in tasks:
            if task not in mp:
                mp[task] = 1
            else:
                mp[task] += 1
            if mp[task] > k:
                k = mp[task]
                top_task = task

        idles = (k-1) * n

        for task in mp:
            if task == top_task:
                continue

            idles -= min(mp[task], k-1)

        return len(tasks) + max(idles, 0) # Idles cannot be negative.
        