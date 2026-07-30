class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix ={}
        postfix ={}


        prefix[0]=1
        postfix[len(nums)-1]=1
        for i in range(1, len(nums)):
                prefix[i]= prefix[i-1]*nums[i-1]
                j= len(nums)-i-1
                postfix[j]=postfix[j+1]*nums[j+1]

        # print(prefix)
        # print(postfix)

        final =[]
        for i in range(0, len(nums)):
            final.append(prefix[i]*postfix[i])

        return final
            
        