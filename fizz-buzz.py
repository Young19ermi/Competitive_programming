class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        test=[]
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                test.append("FizzBuzz")
            elif i%3==0:
                    test.append("Fizz")
            elif i%5==0:
                        test.append("Buzz")
            else:
                            test.append(str(i))
        return test
        
