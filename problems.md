
# Odds and Evens (Last seen 2019-10-17)

Given an array A of non-negative integers, return an array consisting of all the
even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

    Input:  [3,1,2,4]
    Output: [4,2,1,3]

## Extension 1:

Your output array must now be composed of the even array in ascending order, and
the odd array in decending order

    Input:  [3,1,2,4,8,3,4,1]
    Output: [2,4,4,8,3,3,1,1]


# Submatrix (Last seen 2019-10-17)

Given a 2D (binary) matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

    Input: [[1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,0,1,0]]
    Output: 6
    Explanation: A 3*2 rectangle is formed starting at row 1, column 2 and ending
    in row 2 column 4.


# Zero-Sum Game (Last seen 2019-10-24)

Given an array nums of n integers, find all pairs that sum to zero.

    Input:  [-1, 0, 1, 2, -2, -4]
    Output: [[-1, 1], [2, -2]]

## Part B:

Extend this such that you find triples that sum to zero :-)

    Input:  [-1, 0, 1, 2, -2, 2, -4]
    Output: [[-1, 0, 1],[-2, 0, 2], [-4, 2, 2]] 


# Lispy Business (Last seen 2019-10-24)

Given an input containing parenthesies, write a function to decide if the
parentesies are matched. That is, for every opening parenethesis there must be a
respective closing parentesis and vise versa.

    Input:  "((Hello) world))"
    Output: false
    
    Input:  "((((((HELLO))))))World"
    Output: true
    
    Input:  "()()()()()()()123()()()()))(("
    Output: true


# The Legendary Door Problem (Last Seen 2019-10-31)

There are 100 doors in a dungeon. A prisoner, to survive, must execute the
following algorithm:

1. They open all doors. 
2. They close every second door. 
3. They toggle every third door, 

The process continues, for 100 passes, such that for each pass n, the prisoner
toggles every nth door; When the algorithm completes, the evil genius releases
her monsters. The monsters will come out of every open door. 

## Part A:

How many monsters attack her poor prisoner?

## Part B:

Our evil genius likes to make abstract maths a reality. She instead creates d
many doors (where d is any natural number she pleases). Given d many doors, and
d many passes of the algorithm, express the number of monsters that attack their
poor prisoner as a function f(d)


# Sorted Stacking (Last Seen 2019-10-31)

Mix up in groups of first, second, and third years (as possible) and write a
program to sort a stack with the smallest items on top.

Recall that the allowed operations on a stack are: Push, Pop, Peek and isEmpty. 

## Part A:
You are allowed to use exactly one aditional stack. How fast can you go?

## Part B:
You are allowed to use as many additional stacks as you like. How fast can you
go?


# Binary Neighbours (Last seen 2019-11-07)

Given a positive integer, print the next smallest and next largest numbers that
have the same number of 1 bits in their binary representation. Assume it is
even.

## Part B:
If you want to have a really, really tough problem, try it for any positive
integer.


# Say a Word, Any Word (Last seen 2019-11-14)

Given any integer n in range (-2000000000,2000000000) (That is -2 bilion to +2
bilion), produce a string that represents it in natural English language.

    Input:  1234
    Output: One Thousaind Two Hundred (and) Thirty Four
    
    Input:  -92435
    Output: Minus Ninety-two Thousaind Four Hundred (and) Thirty Five


# (Shut up and) Calculate (Last seen 2019-11-14)

You have a computer that only 'knows' addition and negation of integers (E.g.
can turn -4 to 4 and 4 to -4). Do each of these in turn:

1. Define subtraction using only the above two operations
2. Define multiplication using the above three operations
3. Define division using the above four operations.

Hint: You may not need all available operations for each part.


# Magic Indices (Last seen 2019-11-21)

A magic index in an array of n integers (index from 0 to n-1) is defined to be
an index such that a[i] = i.

## Part A:

The array is unsorted, what is the most efficient algorithm that can be written
(i.e. write an algorithm that takes O(_) time, and provide an argument why you
can't go faster than O(_) time)

## Part B:

The list of integers is sorted in the array. Repeat Part A.


# Zero the Matrix (Last seen 2019-11-21)

Write an algorithm such that if an element is in an N by M matrix is zero, the
entire row and column are set to zero.

    Input:   [[1,2,3,4]
              [1,0,8,7]
              [4,4,0,2]
              [6,7,8,9]
              [1,2,3,4]]
    
    Output:  [[1,0,0,4]
              [0,0,0,0]
              [0,0,0,0]
              [6,0,0,9]
              [1,0,0,4]]

## Part B:

What is the time and space complexity of your algorithm?

## Part C:

Can you do this without copying the matrix?


# Problem 1: (Last seen 2019-11-28)

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the
   previous row.

    Matrix = [[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]] Target = 3
              Output: true

How fast can you go, and why?



# Problem 2: (Last seen 2019-11-28)

Write a method to count the number of twos (2) that appear between the number 0
and n (For a given n).

    Input: 25
    Output: 9
    Why?: 2, 12, 20, 21, 22, 23, 24, 25

## Part A:

Assume n < 10000. How fast can you go?

## Part B:

Now there are no restrictions on the value of n. How fast can you go?


# Problem 1: (Last seen 2019-12-05)

Given a list of daily temperatures, return a list such that, for each day in the
input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0
instead.

     Input:  [73, 74, 75, 71, 69, 72, 76, 73]
     Output: [ 1,  1,  4,  2,  1,  1,  0,  0]

## Part B:

Can you do this in linear time?


# Problem 2: (Last seen 2019-12-05)

Given a matrix consisting of 0s and 1s, we may choose any number of columns in
the matrix and flip every cell in that column. Flipping a cell changes the value
of that cell from 0 to 1 or from 1 to 0. Return the maximum number of rows that
have all values equal after some number of flips.

    Input: [[0,1],[1,1]]
    Output: 1
    Explanation: After flipping no values, 1 row has all values equal.

    Input: [[0,1],[1,0]]
    Output: 2
    Explanation: After flipping values in the first column, both rows have equal values.

    Input: [[0,0,0],[0,0,1],[1,1,0]]
    Output: 2
    Explanation: After flipping values in the first two columns, the last two rows have equal values.


# Problem 1: (Last seen 2020-02-27)

Write code to partition a linked list around a value X s.t. all nodes less than
X come before all nodes greater than or equal to X. The two partitions should
preserve their order.

     Input:  3->5->8->5->10->2->1
     Parititon on: 5
     Output: 3->2->1->5->8->5->10


# Problem 2: (Last seen 2020-02-27)

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


# Problem 1: (Last seen 2020-03-12)

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum
equals the given sum.

    Sum: 22
    Tree: 5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    Output: [
              [5,4,11,2],
              [5,8,4,5]
            ]

## Extension 1:

If this was a binary search tree would this make a difference?


# Problem 2: (Last seen 2020-03-12)

Given an array where elements are sorted in ascending order, convert it to a
balanced (as possible) BST.

Hint: CS115 has already given you two very useful algorithms for this ;)

    Input: [-10,-3,-1,0,2,5,9]
    Output:  0
            / \
           /   \
         -3     5
        / \    / \
      -10 -1  2   9


# Problem 3: (Last seen 2020-03-12)

Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

    k: 1
    Tree: 3
         / \
        1   4
         \
          2
    Output: 1


# Problem 1: (Last seen 2020-10-20)

There are 100 closed lockers in a hallway. Behind the lockers are mosnters. On
round 1, you go through the lockers and open every single one. On round 2, you
go through the lockers and shut every second. On round 3, you go through the
lockers and toggle every thrid. On round N, you go through the lockers and
toggle every Nth. After 100 rounds, the monsters will exit the open lockers and
attack. How many monsters will there be attacking you?

## Extension 1:

Instead of 100 lockers, you now have N lockers and N rounds. Solve the same
problem :-)

## Extension 2:

Now, you have N lockers and M rounds, where N and M are not nessesarily the same
number. Solve the same problem once more.


# Problem 2: (Last seen 2020-10-20)

You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test
strips which can be used to detect poison.

A single drop of poison will turn the test strip positive permanently. 

You can put any number of drops on a test strip at once and you can reuse a test
strip as many times as you'd like (as long as the results are negative).
However, you can only run tests once per day, and it takes seven days to return
a result.

How would you figure out the poisoned bottle in as few days as possible? 


# Problem 1: (Last seen 2020-10-27)

A bunch of people are living on an island, when a visitor comes with a strange
order: all blue-eyed people must leave the island as soon as possible. There
will be a flight of unlimited capacity out at 8:00pm every evening. Each person
can see everyone else's eye colour, but they do not know their own (nor can they
find out through someone or something else). Additionally, they do not know how
many people have blue eyes, although they do know that at least one person does.
How many days will it take the blue-eyed people to leave?

Hint: You can assume the people are all equally intelligent, and if one can
think in a specific way, then all of them can. 

Note: Solutions via proxy, i.e. "Invent a reflective surface to look at
yourself" or "Invent a machine that tells you your eye colour" are not
acceptable. This is a logic riddle!


# Problem 2: (Last seen 2020-10-27)

In the new post-apocalyptic world, the world queen is desperately concerned
about the birth rate. Therefore, she decrees that all families should ensure
that they have one girl or else they face massive fines. If all families abide
by this policy -that is, they continue to have children until they have one
girl, at which point they immediately stop- what will the sex ratio of the new
generation be? (Assume that the odds of someone having a boy or a girl on any
given pregnancy is equal.) 

Note: This problem can be solved logically, and by computer simulation. It is up
to you to decide how you choose to solve it, but we recommend you try writing
the simulation first, and then try to logically reason about the result. 

Side-note: If you are unsure how to program the simulation, or if you are just
starting with programming in Java and you need some help let us know! If you are
confident with programming, look out for others you can help :-)


# Problem 1: (Last seen 2020-11-03)

You're on a game show and there's 3 doors, which are all shut.

The game show host asks you to pick a door. You pick a door and then the game
show host opens a door other than the one you picked, to reveal a pair of goats.
She says: "Behind one of the remaining doors is a goat and behind the other door
is a luxurious car". What is the best strategy to win the car?

1. Hold on to the door you selected originally
2. Switch and select the other door

Or, are the two strategies leading to the same result? Try writing a simulation
for this problem and report on the results :-)


# Problem 2: (Last seen 2020-11-03)

You're outside a room with the door shut. There are three light switches on the
wall next to you and three antique lamps inside. You're allowed to open the door
and walk into the room exactly once. That is the only time when you can observe
the lamps. Before you open the door you are allowed to play with the light
switches as much as you like. Your task is to determine which light switch
corresponds to which lamp.


# Problem 3: (Last seen 2020-11-03)

You want to sort an array of numbers. However, you have a problem. You are a
dictator and your philosophy is: if something doesn't follow your rules, kill
it! Let's introduce Stalin Sort:

1. You have an array of random positive integers. 
2. In this array, if a number is 'out of order' it shall be deleted (killed).
3. At the end of the algorithm, all numbers should appear consecutively with any
   open spaces appearing at the end of the array.

What's the fast implementation of Stalin Sort? **Automatic weapons are not
allowed and since cloning technology is not available, you must perform it
in-place. Stalin is merciful, and allows you to place a tombstone value of -1
for each dead number.**

    Input:  [4, 17, 5, 6, 12, 1, 9]
    Output: [4, 5, 6, 9, -1, -1, -1]


# Problem 1: (Last seen 2020-11-10)

Given two strings s1, s2 where length(s1) < length(s2) find the index of the
first instance where s1 is a substring of s2.

    Input: s1 = "abCd", s2 = "ffffabCdCefg"
    Output: 4

## Extension task:

Extend this to return the index of all substrings of s1 in s2.


# Problem 2: (Last seen 2020-11-10)

Given the strings s1, s2, and s3, where length(s1) + length(s2) = length(s3),
determine if you can interleave the characters in s1 and s2 to get to s3.

    Input: s1 = "aadcc", s2 = "beebt", s3 = "aabeedcbtc"
    Output: true
    
    Input: s1 = "aadcc", s2 = "xeebt", s3 = "aabeedcbtc"
    Output: false

## Part A:

No character in s1 appears in s2 and vise-versa

## Part B:

No such restriction applies (i.e. s1 = "aabc", s2 = "aabf")


# Problem 1: (Last seen 2020-11-17)

Given any integer n in range (-2000000000,2000000000) (That is -2 billion to +2
billion), produce a string that represents it in natural English language. 

Note: The "and" is optional but preferred.

    Input : 1234
    Output: One Thousand Two Hundred (and) Thirty Four
    
    Input : -92435
    Output: Minus Ninety-two Thousand Four Hundred (and) Thirty Five


# Problem 2: (Last seen 2020-11-17)

Given a matrix NxN write a method to rotate the matrix by 90 degrees (i.e.
transpose the matrix).

    Input: [[1,2,3],
            [4,5,6],
            [7,8,9]]

    Output: [[7,4,1],
             [8,5,2],
             [9,6,3]]


# Magic Indices (Last seen 2020-11-24)

A magic index in an array of n integers (index from 0 to n-1) is defined to be
an index such that `array[i] == i`.

## Part A:

The array is unsorted, what is the most efficient algorithm that can be written
(i.e. write an algorithm that takes O(_) time, and provide an argument why you
can't go faster than O(_))

## Part B:

The list of integers is sorted in the array. Repeat Part A.


# Problem 2: (Last seen 2020-11-24)

Write a program to swap sequential pairs of odd and even bits in an integer with
as few operations as possible.

    Input:  01010101
    Output: 10101010

    Input:  1011110100
    Output: 0111111000


# Problem 1: (Last seen 2020-12-01)

Given a list of daily temperatures, return a list such that, for each day in the
input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0
instead.

    Input:  [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [ 1,  1,  4,  2,  1,  1,  0,  0]

## Part B:
    Can you do this in linear time?


# Minesweeper (Last seen 2020-12-08)

Design and implement a text-based Minesweeper game. Minesweeper is the classic
single-player computer game where an NxN grid had B mines (or bombs) hidden
across the grid. The remaining cells are either blank or have a number behind
them. The numbers reflect the number of bombs in the surrounding eight cells.

The user then uncovers a cell. If it is a bomb, the player loses. If it is a
number, the number is exposed. If it is a blank cell, this cell and all adjacent
blank cells (up to and including the surrounding numeric cells) are exposed.

The player wins when all non-bomb cells are exposed.

The player can also flag certain places as potential bombs. This doesn't affect
gameplay, other than to block the user from accidentally clicking a cell that is
thought to have a bomb. (Tip: if you're not familiar with this game, please play
a few rounds online first.)


# Problem 1: (Last seen 2021-03-09)

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


# Problem 2: (Last seen 2021-03-09)

Given an M*N matrix of random integers some of which will be zero, zero-out any
row and column where a cell contains a zero. Try to do it in O(M*N) space and
O(M*N) time.

    Input:  1 3 0 7 1 90
            7 8 3 1 3 17
            3 21 2 8 0 3
            1 14 11 3 4 8
    
    Output: 0 0 0 0 0 0
            7 8 0 1 0 17
            0 0 0 0 0 0
            1 14 0 3 0 8
    
    Input:  14 0 7
            8 0 31
            1 4 9
    
    Output: 0 0 0
            0 0 0
            1 0 9

## Extension:

Can you do this in O(1) space and O(M*N) time?


# Problem 1: (Last seen 2021-03-16)

Given a sorted array of integers that contains only the values 1,2 or 3 write a
function to compute the sum of the array.

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


# Problem 2: (Last seen 2021-03-16)

Given an unsorted integer array 'nums', find the smallest missing integer >0

    Input: [1,2,0]
    Output: 3

    Input: [3,4,-1,1]
    Output: 2

    Input: [7,8,9,11,12]
    Output: 1

Constraints:
- The input array length will never exceed 300
- Array elements are in the range of a 32-bit signed integer
