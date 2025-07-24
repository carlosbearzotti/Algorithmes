from typing import List

# My Solution
class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is not None:
                return[hasher.get(i), idx]
            hasher[target-i] = idx

# Gpt -> better solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hasher = {}
#         for idx, num in enumerate(nums):
#             complement = target - num
#             if complement in hasher:
#                 return [hasher[complement], idx]
#             hasher[num] = idx

# Definindo o array e o target
nums = [2, 7, 11, 15]
target = 9

# Criando objeto da classe
sol = Solution()
resultado = sol.twoSum(nums, target)
print(resultado)

# o Gpt complementa dizendo que a busca no sentido de "ir" (Espera seu Target aparecer eo Armazena) tem menos chances de erros e deixa mais claro por isto a opção de busca "vir" (Armazena ao encontrar),
# em termos de otimização ambas executam no mesmo tempo mas a segunda tem menos chance de falhar.