class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        def quickSort(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            if s > e or s < 0 or e > n - 1 or e < 0:
                return arr
            left = s
            pivot = e
            pivot_dist = arr[pivot][0] ** 2 + arr[pivot][1] ** 2
            for i in range(s, e):
                cur_dist = arr[i][0] ** 2 + arr[i][1] ** 2
                if cur_dist < pivot_dist:
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = tmp
                    left += 1
            tmp = arr[left]
            arr[left] = arr[pivot]
            arr[pivot] = tmp
            if left == k or left == k - 1:
                return
            elif left < k - 1:
                quickSort(arr, left + 1, e)     
            else:
                quickSort(arr, 0, left - 1)          
            return arr

        quickSort(points, 0, n - 1)
        return points[:k]
