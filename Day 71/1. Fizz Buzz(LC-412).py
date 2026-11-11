#code

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans












I will iterate through every integer from 1 to n and check its divisibility.

First, I check whether the number is divisible by both 3 and 5. If it is, I append FizzBuzz to the result.

Otherwise, if it is divisible by 3, I append Fizz. If it is divisible by 5, I append Buzz.

If none of these conditions is satisfied, I convert the number into a string and append it to the result.

Finally, I return the result array



#complexity

-Time complexity: (O(n)) — We iterate from 1 to n once, performing a constant number of checks per iteration.

-Space complexity: (O(n)) — We store n strings in the output list.


