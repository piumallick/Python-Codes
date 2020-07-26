# A child is running up a staircase with n steps and 
# can hop either 1 step, 2 steps or 3 steps at a time. 
# Implement a method to count how many possible ways the 
# child can run up the stairs.

def TripleHopRecursive(n, memo):
  if n < 0:
      return 0
  memo[0] = 1
  if n >= 1:
      memo[1] = 1
  if n >= 2:
      memo[2] = memo[1] + memo[0]
  if n > 2:
      for i in range(3, n + 1):
          memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
  return memo[n]
        
    
def climbStairs(n):
  memo = [-1] * (n + 1)
  return TripleHopRecursive(n, memo)

n = 3
print(climbStairs(n))

# Output: 4    
