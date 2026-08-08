class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         mmin =0
         mmax = len(matrix)-1
         nmin = 0
         nmax = len(matrix[0])-1

         while mmin <= mmax and nmin <= nmax: 
            mmid = mmin + (mmax - mmin)//2
            nmid = nmin + (nmax - nmin)//2

            if target >= matrix[mmid][nmin] and target <= matrix[mmid][nmax]:
                if target in set(matrix[mmid]):
                    return True
                else:
                    return False
            elif target > matrix[mmid][nmax]:
                mmin = mmid + 1
            elif target < matrix[mmid][nmin]:
                mmax = mmid - 1
        
         return False