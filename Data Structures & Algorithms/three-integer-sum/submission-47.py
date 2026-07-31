class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums =sorted(nums)
        final_list=[]
        l = len(snums)
        i =0
        while i <(l-2):
            print("i is ", i , snums[i], "final list", final_list)
            target = 0 - snums[i]
            left = i+1
            right = l -1
            while left < right:            
                if snums[left]+snums[right] == target:
                    final_list.append([snums[i],snums[left],snums[right] ])
                    left+=1
                    right-=1

                    while left < right:
                        if snums[left]==snums[left-1]:
                            left+=1
                        else: break

                    while right > left:
                        if snums[right]==snums[right+1]:
                            right-=1
                        else: break

                elif snums[left]+snums[right] < target:
                    left+=1
                elif snums[left]+snums[right] > target:
                    right-=1

            while i < l-2:
                if snums[i+1]==snums[i]:
                    print("done passing i", i, snums[i])
                    i+=1
                else: break
            
            i+=1

        return final_list





