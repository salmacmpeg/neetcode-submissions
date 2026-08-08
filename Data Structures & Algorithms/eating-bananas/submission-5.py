class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hopt = 0
        kacc = 0
        kmin = 1
        kmax= max(piles)
        
        while kmin <= kmax:
            kmid = kmin + (kmax -kmin)//2
            hsum = 0
            for elem in piles:
                hsum += -(-elem // kmid)
            if hsum <= h:
                hopt = hsum
                kacc = kmid
                kmax = kmid -1
            elif hsum > h:
                kmin = kmid + 1

        return kacc
