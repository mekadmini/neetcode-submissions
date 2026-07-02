class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product_without_one_zero = 1
        number_zeros = 0
        for num in nums:
            if num != 0:
                total_product_without_one_zero *= num
            else:
                number_zeros +=1
            if number_zeros > 1:
                total_product_without_one_zero = 0
                break
        ls = []
        for num in nums:
            if num == 0:
                ls.append(total_product_without_one_zero)
            elif number_zeros > 0:
                ls.append(0)
            else:
                ls.append(total_product_without_one_zero // num)
        return ls