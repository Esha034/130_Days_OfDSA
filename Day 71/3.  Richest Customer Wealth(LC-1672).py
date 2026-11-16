#code

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        maxwealth=0
        for customer in accounts:
            wealth=0
            for money in customer:
                wealth+=money
            maxwealth=max(wealth,maxwealth)
        return maxwealth

#Intuition:

-I calculate each customers total wealth and keep track of the maximum.

For that, I will use two nested loops to calculate the richest customer's wealth.

The outer loop iterates through each customer, and the inner loop iterates through all the bank accounts belonging to that customer.

I initialize a variable wealth to zero for each customer and add the balance of every bank account to it.

After calculating the customer's total wealth, I compare it with maxwealth and update maxwealth if the current customer's wealth is greater.

After processing all customers, I return maxwealth, which represents the highest total wealth of richest customer.



4. Complexity analysis
Let:
- (m) = number of customers (rows)
- (n) = number of bank accounts per customer (columns)

Time complexity: (O(m times n))
- The outer loop runs (m) times.
- The inner loop processes (n) accounts for each customer.
- Therefore, the total number of operations is proportional to (m * n).

Auxiliary space complexity: (O(1))

We use only two variables, wealth and maxwealth, regardless of the grid size. The input grid is not counted as extra space.



