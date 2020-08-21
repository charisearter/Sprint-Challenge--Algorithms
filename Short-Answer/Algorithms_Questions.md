# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

A) I think this would be O(1) - I say this because no matter what n is you are still only doing the same amount of n in the equation for line 10 and 11. That is why I think it is a constant O(1).

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

B) I think this one is O(n^2). I think this because depending on how large n is, the runtime will change. Also, it is doing 2 loops in the equation for and while. For is the outer loop and while is the inner loop.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: //base case
        return 0

      return 2 + bunnyEars(bunnies-1)  //recursion
```

C) I think this one is O(2^n). n is how many bunnies there are and how deep this function would go. There are 2 cases: there are 0 bunnies or there are bunnies. This is why I figure it is O(2^n) after a bit of research and converting the O(branch ^depth). I am assuming branches is the cases and depth is the input (n).

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Understanding: Find the highest floor where the eggs will not break if dropped while using the least amount of eggs.

Realistically, I would start at the lowest floor and work my way up with these super resilient eggs. I say this because I have an indeterminate amount of floors but am assured I have plenty of eggs. The worst-case scenario would be starting from the topmost floor and work my way down because there is no guarantee that the eggs won't be all gone by the time I get to the pivotal floor where the eggs will not break when dropped.

drop(eggs, floors)
Get base case 10 floors 5 eggs drop(5, 10)
Simulate dropping the number of eggs from each floor to find the worst case. The egg can break or not break.

- Starting from topmost floor drop (5 (no break), total floor (10) - current floor(10)) <-- do this for each floor, floor variable will change depending on what floor you are on and how many are left to go to the top. If the egg does not break, floors will count up, showing the number of floors above left.

- Starting from topmost floor (eggs - 1 (breaks), total floors - 1) <-- do for each floor

Keep going until I get the worst case and then add +1 in order to simulate the drop.

This would be O(eggsTotal _ totlaFloors^2) ... so that would be O(n^2 _ totalEggs)
