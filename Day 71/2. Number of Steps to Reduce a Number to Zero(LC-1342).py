# Optimal code

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num>0:
            if num%2==0:
                num/=2
               
            else:
                num-=1
            count+=1
        return count



#Intuition:

I will use a while loop that continues until the number becomes zero.

In each iteration, I check whether the current number is even or odd using the modulo operator.

If the number is even, I divide it by 2 using integer division. Otherwise, I subtract 1.

After each operation, I increment the step counter by 1. Once the number reaches zero, the loop terminates, and I return the total number of steps.




    
#Complexity analysis:
    
Time complexity: 
(O(log n))
- When the number is even, we divide it by 2, reducing it significantly.
When it is odd, we subtract 1, making it even; the next operation divides it by 2.
Therefore, the number of operations grows logarithmically with the input.
    
Space complexity:
(O(1))
We use only two variables, num and count, regardless of the input size.
