class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billMap = defaultdict(int)
        for bill in bills:
            if bill == 5:
                billMap[5] = 1 + billMap.get(5, 0)
                continue
            elif bill == 10:
                if billMap[5]==0:
                    return False
                else:
                    billMap[5]-=1
                    billMap[10] = 1 + billMap.get(10, 0)
                    continue
            else:
                if billMap[10] and billMap[5]:
                    billMap[10]-=1
                    billMap[5]-=1
                elif billMap[5]>=3:
                    billMap[5]-=3
                else:
                    return False
        return True
                
                    


            

