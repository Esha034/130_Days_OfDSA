My Learning:

Why this code is not correct?


#wrong solution
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans=[0]*3
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans[i]="FizzBuzz"
            elif i%3==0:
                ans[i]="Fizz"
            elif i%5==0:
                ans[i]="Buzz"
            else:
                ans[i]="i"
        return ans

For Input: n = 3
    Output: ["1","2","Fizz"]

It will show 
IndexError: list assignment index out of range.
This happens because your loop runs i from 1 to n (inclusive), but Python lists are 0-indexed. 
So, When i = 3 (for n = 3), ans[3] tries to access index 3 in a list of size 3 (which only has indices 0, 1, and 2), causing the crash.
Also, you need to store string values instead of integers, and use append or map indices properly.










#correct solution


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


#Intuition

I will iterate through every integer from 1 to n and check its divisibility.

First, I check whether the number is divisible by both 3 and 5. If it is, I append FizzBuzz to the result.

Otherwise, if it is divisible by 3, I append Fizz. If it is divisible by 5, I append Buzz.

If none of these conditions is satisfied, I convert the number into a string and append it to the result.

Finally, I return the result array



#complexity

-Time complexity: (O(n)) — We iterate from 1 to n once, performing a constant number of checks per iteration.

-Space complexity: (O(n)) — We store n strings in the output list.


