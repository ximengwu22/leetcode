# This document aims to practice all the OA questions found online.
# including Intern and Full-time positions.

# https://leetcode.com/discuss/interview-question?currentPage=1&orderBy=newest_to_oldest&query=&tag=amazon

# resoruce: https://leetcode.com/discuss/interview-question/3113182/AMAZON-OA-or-SDE-INTERN-2023
'''
Question 1: 
    A recently launched supplemental typing keyboard gained significant popularity on Amazon Shopping due to its flexibility.

    This keypad can be connected to any electronic device and has 9 buttons, where each button can have up to 3 lowercase English letters. The buyer has the freedom to choose which letters to place on a button while ensuring that the arrangement is valid. A keypad design is said to be valid if:
    - All 26 letters of the English alphabet exist on the keypad.
    - Each letter is mapped to exactly one button;
    - A button has at most 3 letters mapped to it.

    Examples of some valid keypad designs are:
    1[abc] 2[def] 3[ghi]        1[ajs] 2[bot] 3[cpu] 
    4[jkl] 5[mno] 6[pqr]        4[dkv] 5[hmz] 6[gl]
    7[stu] 8[vwx] 9[yz]         7[enw] 8[fqx] 9[iry]

    - In the left keypad, "hello" can be typed using the following button presses: [3] twice (prints 'h'), [2] twice (prints 'e'). [4] thrice (prints 'i'), [4] thrice (prints T), [5] thrice (prints 'o'). Thus, total number of button presses = 2 + 2 + 3 + 3 + 3 = 13.
    - In the right keypad, "hello" can be typed using the following button presses: [5] once (prints 'h'), [7] once (prints 'e'), [6] twice (prints T), [6] twice (prints 'i'), [2] twice (prints 'o'). Thus, total number of button presses = 1 + 1 + 2 + 2 + 2 = 8.

    The keypad click count is defined as the number of button presses required to print a given string In order to send messages faster customers tend to set the keypad design in
'''
from collections import Counter
def minKeyoadClickCount(text: str):
    cntr = Counter(text)
    values = sorted(cntr.values(), reverse=True)
    res = 0
    for i in range(len(values)):
        res += (i//9 + 1)*values[i]
    
    return res

print(minKeyoadClickCount("hello"))
print(minKeyoadClickCount("abacadefghibj"))
    
    


'''
Code Question 2:
    Several satellites provide observational black and white images which are stored
    in data centers at Amazon Web Services (AWS).
    A black and white image is composed of pixels and is represented as
    an (n-m) grid of cells. Each pixel can have a value of 0 or 1, where 0 represents a
    white pixel and 1 represents a black pixel. The greyness of a cell (,) is affected by
    the pixel values in the Ah row and the th column. More formally, the greyness of
    the cell (, ) is the difference between the number of black pixels in the throw
    and the th column and the number of white pixels in the throw and the
    th column.
    
    Find the maximum greyness among all the cells of the grid.
    Note: The value of cell (i,j) is counted both in the frow and i-th the j-th column.
    Example:
        pixels = ['101', '001', '110]
        The nxm=3x3 grid of pixels looks like this:
        1 0 1
        0 0 1
        1 1 0
        The greyness of the cell (1, 1) is calculated as:
        Number of 1s in 1st row = 2
        Number of 1s in 1st column = 2
        Number of Os in 1st row = 1
        Number of Os in 1st column = 1
'''


# https://leetcode.com/discuss/interview-question/1761729/amazon-new-grad-oa-pascal-triangle-decryption
'''
Pascal Triangle Decryption: 

Given an array of integers, we sum neighbouring elements like pascal's triangle until only two integers remain and take those to be the output. During the process, if the sum of two elements is greater than or equal to 10, we only take the digit place to the next level. Sorry if the description isn't clear enough, I included a picture to demonstrate the idea.
4 + 5 + 6 + 7
  9 + 1 + 3
    0   4   <-- Output is 04 
'''


# https://leetcode.com/discuss/interview-question/2408607/Amazon-2023-New-GRAD-OA
'''
leetcode 719
'''
'''
An Amazon team is being formed to work on a new project. They will choose a pair of developers according to their skills. The inefficiency of a team is defined as the
absolute difference between the skills of the two developers. Given the skill values of n developers, find the k teams with the lowest inefficiencies among all possible pairs of teams. 
Return their inefficiencies sorted ascending.
Note: Pair (i, j) is considered the same as pair (j, i).
Example
If n = 3, skill = [6, 9, 1], k = 2
The following pairs of teams are possible:
Team No.    Skill 1     Skill 2     Inefficiency
1           6           9           | 6 - 9 | = 3
2           6           1           | 6 - 1 | = 5
3           9           1           | 9 - 1 | = 8

- The first 2 smallest numbers among [3, 5, 8] are 3 and 5. 
- Return the array [3, 5]. Note that the array is sorted ascending.

Function Description
Complete the function
getSmallestinefficiencies in the editor below.
getSmallestinefficiencies has the following parameters:
- int skill[n]: the skill values for n developers
- int k: the number of pairs required

Returns
    int[k]: the k smallest inefficiencies in sorted order
Constraints
    - 2 ≤ n ≤ 105
    - 1 ≤ skill[1] ≤ 108
    - 1 ≤ k ≤ min (2* 10^5, n*(n-1)/2)
'''


# https://leetcode.com/discuss/interview-question/3714701/Amazon-OA
'''
There are n event records of d players who participated in different events in form of [race id, player's id, player's time]. For some race id, a player's ranking is decided based on the increasing order of their finish time. If two players have the same finish time, the one with a lower id is ranked lower.
The average standing of any player is the average of their various positions in all the races they competed in, expressed in the form of a fraction p/q. If there are multiple possible such fractions, reduce them such that p is the minimum possible.
Return a 2-dimensional array where each element i contains the ith player's p and q as described above.
If the player did not compete in any races, the player's p and values are both - 1.
Example
For example, if n = 3, d = 3, and records = [[1, 1, 100]], [1, 2, 200], [2, 1, 500]].
There are a total of d = 3 players.

Player 0 did not compete in any race, so P0 = -1 and Q0=-1.
Player 1 competed in 2 races and came first in both. Their average standing is (1+1)/2. Reduce as described
so P1 = 1 and Q1 = 1.
Player 2 competed in 1 race and came second. Their average standing is (2)/1. Thus, P2 = 2 and Q2 = 1.
Return [[-1, -1], [1, 1], [2, 1]].
'''

# https://leetcode.com/discuss/interview-question/2347635/Amazon-or-SDE-1-2023-or-OA

# https://leetcode.com/discuss/interview-question/2439597/Amazon-OA-2023

# https://leetcode.com/discuss/interview-question/3714711/Amazon-OA-2023
'''
Suppose that Amazon has marked n strings that are prohibited in reviews. They assign a score to each review that denotes how well it follows the guidelines. The score of a review is defined as the longest contiguous substring of the review which does not contain any string among the list of n prohibited strings. A string contains a prohibited word if it has a contiguous substring that matches a word from the prohibited list, ignoring the case.
Given a review and a list of prohibited strings, calculate the review score.
Example
review = "GoodProductButScrapAfterWash"
prohibitedWords = ['crap", "odpro"]
Some of the substrings that do not contain a prohibited word are:
• ProductBut
• rapAfterWash
• dProductButScu
• Wash
The longest substring is "dProductButScra", return its length, 15.

https://leetcode.com/problems/length-of-the-longest-valid-substring/discuss/ 
'''


