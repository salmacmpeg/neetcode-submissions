class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_pairs=[ (p,s) for p,s in zip(position, speed)]
        cars_pairs.sort(reverse=True)

        s = []
        for elem in cars_pairs:
            rem = (target - elem[0])/ elem[1]
            if len(s)==0 or rem > s[-1]:
                s.append(rem)

        return len(s)
        