class MedianFinder:

    def __init__(self):
        self.numbers = []
        

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.numbers)
        while l < r:
            mid = (l + r) // 2
            if self.numbers[mid] > num:
                l = mid + 1
            else:
                r = mid
        self.numbers.insert(l, num)
        print(self.numbers)


    def findMedian(self) -> float:
        n = len(self.numbers)
        if  n % 2 == 0:
            return (self.numbers[n//2-1] + self.numbers[n//2]) / 2
        return self.numbers[n//2]

        
        