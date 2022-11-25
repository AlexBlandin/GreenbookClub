
# Odds and Evens (Last seen 2019-10-17)

Given an array `A` of non-negative integers, return an array consisting of all
the _even_ elements of `A`, followed by all the _odd_ elements of `A`.

You may return any answer array that satisfies this condition.

    Input:  [3,1,2,4]
    Output: [4,2,1,3]

## Extension:

Your output array must now be composed of the even array in ascending order, and
the odd array in descending order.

    Input:  [3,1,2,4,8,3,4,1]
    Output: [2,4,4,8,3,3,1,1]


# Submatrix (Last seen 2022-11-14)

Given a 2-dimensional array filled with `0`s and `1`s (a binary matrix), find the
largest rectangle containing only `1`s and return its area.

    Input: [[1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,0,1,0]]
    Output: 6
    Explanation: A 3*2 rectangle is formed starting at row 1, column 2 and ending
    in row 2 column 4.


# Zero-Sum Game (Last seen 2022-03-17)

Given an array of `n` integers, find all pairs that sum to zero.

    Input:  [-1, 0, 1, 2, -2, -4]
    Output: [[-1, 1], [2, -2]]

## Part B:

Extend this such that you find triples that sum to zero :-)

    Input:  [-1, 0, 1, 2, -2, 2, -4]
    Output: [[-1, 0, 1],[-2, 0, 2], [-4, 2, 2]] 

# Countdown Numbers Game (Last seen 2022-03-17)

Given an array of `n` integers, find all equations using `+`, `-`, `×`, and `÷` over `k` elements (no using the same element twice in the equation, same values are okay) that `= 24`.

# Lispy Business (Last seen 2021-11-08)

Given an input containing parentheses, write a function to decide if the
parentheses are matched. That is, for every opening parenthesis there must be a
respective closing parenthesis and vice-versa.

    Input:  "((Hello) world))"
    Output: false
    
    Input:  "((((((HELLO))))))World"
    Output: true
    
    Input:  "()()()()()()()123()()()()))(("
    Output: true

Extension: As you see, the third example matched, despite there being "opening"
parenthesis AFTER their "closing" pair. Tighten your system such that this is no
longer true, such that each opening `(` comes before its paired closing `)`.

# The Legendary Door Problem (Last Seen 2022-10-31)

There are 100 closed lockers in a hallway. Behind the lockers are monsters. On
round 1, you go through the lockers and open every single one. On round 2, you
go through the lockers and shut every second. On round 3, you go through the
lockers and toggle every third. On round N, you go through the lockers and
toggle every Nth. After 100 rounds, the monsters will exit the open lockers and
attack. How many monsters will there be attacking you?

Extension 1: Instead of 100 lockers, you now have N lockers and N rounds. Solve
the same problem :-)

Extension 2: Now, you have N lockers and M rounds, where N and M are not
necessarily the same number. Solve the same problem once more.


# Sorted Stacking (Last Seen 2019-10-31)

Write a program to sort a stack with the smallest items on top.

Recall that the allowed operations on a stack are: `push`, `pop`, `peek` and
`is_empty`. 

## Part A:
You are allowed to use exactly one additional stack. How fast can you go?

## Part B:
You are allowed to use as many additional stacks as you like. How fast can you
go?


# Binary Neighbours (Last seen 2022-11-21)

Given a positive integer, print the next smallest and next largest numbers that
have the same number of 1 bits in their binary representation. Assume it is
even.

## Part B:
If you want to have a really, really tough problem, try it for any positive
integer.


# (Shut up and) Calculate (Last seen 2019-11-14)

You have a computer that only 'knows' addition and negation of integers (E.g.
can turn -4 to 4 and 4 to -4). Do each of these in turn:

1. Define subtraction using only the above two operations
2. Define multiplication using the above three operations
3. Define division using the above four operations.

Hint: You may not need all available operations for each part.


# Magic Indices (Last seen 2021-11-22)

A magic index in an array of `n` integers (index from `0` to `n-1`) is defined
to be an index such that `array[i] == i`.

## Part A:

The array is sorted, what is the most efficient algorithm that can be written
(i.e. write an algorithm that takes `O(_)` time, and provide an argument why you
can't go faster than `O(_)` time)

    Input: {0, 1, 2, 3}
    Output: true

    Input: {0, 0, 0, 2, 4}
    Output: true

    Input: {1, 2, 3, 5}
    Output: false

## Part B:

The array of integers is now unsorted. How fast can you go?

# Something Similar (Last seen 2021-11-22)

Given two strings, write a method to decide if one is a permutation of the other.

    Input: "abc", "bca"
    Output: true
    
    Input: "abcd", "abc"
    Output: false
    
    Input: "The quick brown fox jumps over the lazy dog",
           "ty oduohmq ruwebe v czeprf iaht jolsxn o gk"
    Output: false -- This is case sensitive!

# Zero the Matrix (Last seen 2021-11-08)

Write an algorithm such that if an element in an `N x M` matrix is zero, the
entire row and column of that element are set to zero.

Given an `N x M` matrix of random integers, some of which will be zero, zero-out
any row and column where a cell contains a zero.

    Input:  1 2 3 4
            1 0 8 7
            4 4 0 2
            6 7 8 9
            1 2 3 4
    
    Output: 1 0 0 4
            0 0 0 0
            0 0 0 0
            6 0 0 9
            1 0 0 4
    
    Input:  14 0  7
             8 0 31
             1 4  9
    
    Output: 0 0 0
            0 0 0
            1 0 9

## Part B:

What is the time and space complexity of your algorithm?

## Part C:

Can you do this in `O(1)` space and `O(N x M)` time?


# Matrix Search (Last seen 2019-11-28)

Write an efficient algorithm that searches for a value `x` in an `N x M` matrix.
This matrix has the following properties:

1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the
   previous row.

If we are searching for `x=3`, our output is its position:

    Input: [[01, 03, 05, 07],
            [10, 11, 16, 20],
            [23, 30, 34, 50]]
    Output: (0,1)

Note: If the value is not in the matrix, you can return `(-1,-1)` or something
signifying it was not found (`None`, `Nothing`, `null`, etc.)

How fast can you go, and why?


# Too Many Twos (Last seen 2019-11-28)

Write a method to count the number of twos (`2`) that appear between the number
`0` and `n` (for a given `n`).

    Input: 25
    Output: 9
    Why?: 2, 12, 20, 21, 22, 23, 24, 25

## Part A:

Assume `n` < 10000. How fast can you go?

## Part B:

Now there are no restrictions on the value of `n`. How fast can you go?


# Top Temperatures (Last seen 2020-12-01)

Given a list of daily temperatures, return a list such that, for each day in the
input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0
instead.

     Input:  [73, 74, 75, 71, 69, 72, 76, 73]
     Output: [ 1,  1,  4,  2,  1,  1,  0,  0]

## Part B:

Can you do this in linear time?


# Matrix Flipper (Last seen 2022-11-21)

Given a matrix consisting of `0`s and `1`s, we may choose any number of columns
in the matrix and flip every cell in that column. Flipping a cell changes the
value of that cell from `0` to `1` or from `1` to `0`. Return the maximum number
of rows that have all values equal after some number of flips.

    Input: [[0,1],
            [1,1]]
    Output: 1
    Explanation: After flipping no values, 1 row has all values equal.

    Input: [[0,1],
            [1,0]]
    Output: 2
    Explanation: After flipping values in the first column, both rows
                 have equal values.

    Input: [[0,0,0],
            [0,0,1],
            [1,1,0]]
    Output: 2
    Explanation: After flipping values in the first two columns,
                 the last two rows have equal values.


# Partition Petition (Last seen 2020-02-27)

Write code to partition a linked list around a value `X` such that all nodes
less than `X` come before all nodes greater than or equal to `X`. The two
partitions should preserve their order.

     Input:  3->5->8->5->10->2->1
     Parititon on: 5
     Output: 3->2->1->5->8->5->10


# Around and Around and (Last seen 2020-02-27)

Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop. A circular linked list is a corrupted linked list in
which a node's next pointer points to an earlier node in the linked list as to
make a loop.

    Input:  a->b->c->d->e-+
                  ^       |
                  |       |
                  +-------+
    Output: c

This problem has many possible methods. Try to come up with a few :-)


# Path Sums (Last seen 2020-03-12)

Given a binary tree and a sum, find all root-to-leaf paths where have a sum of
values/labels equal to the given sum.

    Sum: 22
    Tree: 5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    Output: [[5,4,11,2],
             [5,8,4,5]]

## Extension:

If this was a binary search tree would this make a difference?


# Balancing Lists (Last seen 2020-03-12)

Given an array where elements are sorted in ascending order, convert it to a
balanced binary search tree (as balanced as possible, at least).

Hint: CS115 has already given you two very useful algorithms for this ;)

    Input: [-10,-3,-1,0,2,5,9]
    Output:  0
            / \
           /   \
         -3     5
        / \    / \
      -10 -1  2   9


# Searching the Search Tree (Last seen 2020-03-12)

Given a binary search tree, write a function to find the `N`th smallest element
in it.

    N: 1
    Tree: 3
         / \
        1   4
         \
          2
    Output: 1


# Deadly Soda (Last seen 2022-10-31)

You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test
strips which can be used to detect poison. A single drop of poison will turn the
test strip positive permanently. You can put any number of drops on a test strip
at once, and you can reuse a test strip as many times as you'd like (as long as
the results are negative). However, you can only run tests once per day, and it
takes seven days to return a result. How would you figure out the poisoned
bottle in as few days as possible?


# Island of Paradise (Last seen 2020-10-27)

A bunch of people are living on an island, when a visitor comes with a strange
request: all blue-eyed people must leave the island as soon as possible. There
will be a flight of unlimited capacity out at 8:00pm every evening. Each person
can see everyone else's eye colour, but they do not know their own (nor can they
find out through someone or something else). Additionally, they do not know how
many people have blue eyes, although they do know that at least one person does.
How many days will it take the blue-eyed people to leave?

Hint: You can assume the people are all equally intelligent, and if one can
think in a specific way, then all of them can. 

Note: Solutions via proxy, i.e. "Invent a reflective surface to look at
yourself" or "Invent a machine that tells you your eye colour" are not
acceptable. This is a logic puzzle!


# The Legally Distinct Minty Hill Problem (Last seen 2022-11-07)

You're on a game show and there are 3 doors, which are all shut.

The game show host asks you to pick a door. You pick a door and then the game
show host opens a door other than the one you picked, to reveal a pair of goats.
She says: "Behind one of the remaining doors is a goat and behind the other door
is a luxurious car". What is the best strategy to win the car?

1. Hold on to the door you selected originally
2. Switch and select the other door

Or, are the two strategies leading to the same result? Try writing a simulation
for this problem and report on the results :-)


# L A M P (Last seen 2020-11-03)

You're outside a room with the door shut. There are three light switches on the
wall next to you and three antique lamps inside.

You're allowed to open the door and walk into the room exactly once. That is the
only time when you can observe the lamps. Before you open the door you are
allowed to play with the light switches as much as you like.

Your task is to determine which light switch corresponds to which lamp.


# Array Sort You! (Last seen 2022-11-07)

You want to sort an array of numbers. However, you have a problem. You are a
dictator and your philosophy is: if something doesn't follow your rules, kill
it! Let's introduce Stalin Sort:

1. You have an array of random positive integers. 
2. In this array, if a number is "out of order" it shall be killed.
3. At the end of the algorithm, all numbers should appear consecutively. Any
   open spaces (if any) can only appear at the end of the array.

What's the fast implementation of Stalin Sort? **Automatic weapons are not allowed.**

    Input:  [4, 17, 5, 6, 12, 1, 9]
    Output: [4, 5, 6, 9]

## Extension:

Since cloning technology is not available, you must perform it in-place. **Stalin is merciful, and allows you to place a tombstone for each dead number.** Tombstones let you know a number was killed, and represent the empty spaces at the end of the array. However, tombstones must be compliant with state law on standardised cemetary supplies, so better make those tombstones the value -1.

    Input:  [4, 17, 5, 6, 12, 1, 9]
    Output: [4, 5, 6, 9, -1, -1, -1]


# Substring (Last seen 2022-11-07)

Given two strings `s1` and `s2`, where `length(s1) < length(s2)`, find the index
of the first instance where `s1` is a substring of `s2`.

    Input: s1 = "abCd", s2 = "ffffabCdCefg"
    Output: 4

## Extension:

Return the index of all substrings of `s1` in `s2`.


# Interleaved Intermission (Last seen 2020-11-10)

Given strings `s1`, `s2`, and `s3`, where `length(s1) + length(s2) = length(s3)`,
determine if you can interleave the characters in `s1` and `s2` to get `s3`.

    Input: s1 = "aadcc", s2 = "beebt", s3 = "aabeedcbtc"
    Output: true
    
    Input: s1 = "aadcc", s2 = "xeebt", s3 = "aabeedcbtc"
    Output: false

## Part A:

The strings `s1` and `s2` do not share any characters.

## Part B:

The strings `s1` and `s2` can contain any characters (i.e. `s1 = "aabc"`, `s2 = "aabf"`).


# Say a Word, Any Word (Last seen 2021-11-29)

Given any integer `n` in range (-2000000000,2000000000) (That is -2 billion to
+2 billion), produce a string that represents it in natural English language. 

Note: The "and" is optional but preferred.

    Input : 1234
    Output: One Thousand Two Hundred (and) Thirty Four
    
    Input : -92435
    Output: Minus Ninety-two Thousand Four Hundred (and) Thirty Five


# Matrix Revolutions (Last seen 2022-11-14)

Given an `N x N` matrix, write a method to rotate the matrix by 90 degrees (a "transpose").

    Input: [[1,2,3],
            [4,5,6],
            [7,8,9]]

    Output: [[7,4,1],
             [8,5,2],
             [9,6,3]]

## Extension:

How fast can you go? Can you do this with `O(1)` space?

## Extension Reloaded:

How fast can you transpose the matrix (flip it over a diagonal)?

    Input: [[1,2,3],
            [4,5,6],
            [7,8,9]]

    Output: [[1,4,7],
             [2,5,8],
             [3,6,9]]

Can you do this in `O(1)` space?


# Odd Bitswap Even (Last seen 2022-03-17)

Write a program to swap sequential pairs of odd and even bits in an integer with
as few operations as possible.

    Input:  01010101
    Output: 10101010

    Input:  1011110100
    Output: 0111111000


# Minesweeper (Last seen 2021-12-06)

Design and implement a text-based Minesweeper game. Minesweeper is the classic
single-player computer game with an `N x N` grid and `B` mines (or bombs)
hidden across the grid. The remaining cells are either blank or have a number
behind them. The numbers reflect the number of bombs in the surrounding eight
cells.

The user then uncovers a cell. If it is a bomb, the player loses. If it is a
number, the number is exposed. If it is a blank cell, this cell and all adjacent
blank cells (up to and including the surrounding numeric cells) are exposed.

The player wins when all non-bomb cells are exposed.

The player can also flag certain places as potential bombs. This doesn't affect
gameplay, other than to block the user from accidentally clicking a cell that is
thought to have a bomb.

Tip: If you're not familiar with this game, you can play a few rounds online
https://minesweeperonline.com/

Extension:

Have fun with this! Here's a few ideas:

- Give this a non-text-based GUI
  - Mouse controls
  - Sound effects
- Different rulesets?
  - Logical/no-guess/pure-skill minesweeper
  - Difficulty settings (more mines?)
  - "Fair" minesweeper (safe first click)
  - "Tentaizu" minesweeper (unique solution + only partially uncovered)
- Different boards
  - Board sizes
  - Hexagonal cells
  - 3D minesweeper (can play a first-person one here https://krzyhau.itch.io/mine-shaft)
- Different algorithms!
  - Flood clear safe tiles
  - Tighter/wider clusters of mines
- Multiplayer (doesn't have to be online, as that's a lot more effort) 
  - Various examples to look at, such as https://minesweeper-multiplayer.dk/about
  - Mix in above, such as hexagonal tiles https://www.multisweeper.com

# Word Sort (Last seen 2021-03-09)

You are given a string containing multiple words. Your output is the same
string, except that each word has had its characters sorted.

    Input: "hello world"
    Output: "ehllo dlorw"
    
    Input: "welcome back to green book club"
    Output: "ceelmow abck ot eegnr bkoo bclu"

## Extension:

How fast can you do this? What about if you are constrained to at-most 4
different letters per word? Any number of repetitions are allowed, such as:
    
    Input: "green book club is so much fun"
    Output: "eegnr bkoo bclu is os chmu fnu"


# Sum 123s (Last seen 2021-03-16)

Given a sorted array of integers that contains only the values 1, 2, or 3, write
a function to compute the sum of the array.

    Input:  [1,1,1,1,1,1,2,2,3,3,3,3,3,3]
    Output: 28

    Input:  [1,2,3]
    Output: 6
        
    Input:  [1,3]
    Output: 4

    Input:  [1,1,1,1,3,3]
    Output: 10

## Extension:

Can you solve this problem in less than O(n) time?


# A Little Missing Something (Last seen 2022-11-21)

Given an array of integers, find the smallest missing integer greater than 0.

    Input: [1,2,0]
    Output: 3

    Input: [3,4,-1,1]
    Output: 2

    Input: [7,8,9,11,12]
    Output: 1


# Letterful Substring

Given the string S of length N, determine the length of the longest substring in
which the number of occurrences of each letter in that substring are equal.

    Input: "ababbcbc"
    Output: 4
    
    Input: "aabcde"
    Output: 5
    
    Input: "aaaa"
    Output: 4
    
    Input: "daababbd"
    Output: 6


# Water Trap (Last seen 2021-11-29)

Imagine a histogram (bar graph). Design an algorithm to compute the volume of
water it could hold if someone poured water across the top. You can assume that
each histogram bar has width 1. (Says "volume" but really it's area since 2D.)

    Input: {0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0}
    Output: 26

Can visualise the problem if you wish, the above example looks like:

```
     #
     #~~~~#
  #~~#    #
  #  #  # #
  #  #  # #
  #  #  # #~#
---------------- (height=0) # = solid, "~" = waterline
0040060030501000
```

(Green book page 189)

## Extension:

Extend this a dimension! (Only after you've done the original problem. Concentrate on that first!)

# Swan Ponds (Last seen 2021-11-29)

You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of zero indicates water.
A pond is a region of water connected vertically, horizontally, or diagonally. The size of the pond is the total number of connected water cells.

Write a method to compute the sizes of all ponds in the matrix.

    Input:  0 2 1 0
            0 1 0 1
            1 1 0 1
            0 1 0 1
    Output: 2, 4, 1 (in any order)

    Input:  0 1 0
            1 0 1
            0 1 0
    Output: 5 (observe they're all connected diagonally)