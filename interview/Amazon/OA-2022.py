# https://leetcode.com/discuss/interview-question/1910880/amazon-sde-2-oa
"""
There are 3 types of exercises in the assessment:

Coding Challenge – this timed section takes 90 minutes, work through two coding problems.
Work Simulation – typically takes 15 minutes, work through software development decisions faced by SDEs at Amazon.
Work Style Surveys – typically takes 10 minutes, 2 surveys - answer questions about how you approach software engineering work and your approach to work in general.
Coding Challenge

Q1 : Given an array denoting shipment counts at each warehouses, calculate how many days it would take ship them all, if equal number of shipments can only be shipped from each warehouse having non-zero shipment.
Example - [4,2,3,3,3] -> it would take 3 days
2 shipments from each warehouse on 1st day => [2,0,1,1,1]
1 shipment from each warehouse on 2nd day => [1,0,0,0,0]
1 shipment from the 1st warehouse on 3rd day
My Approach:

The idea is that one can remove minimum value from array at once
Sort the array in ascending order
Traverse the array, keeping the shipments count already shipped from a single warehouse. So instead of actual subtracting the shipments I just kept the count.
Time - O(NLogN + N)

Q2 : Given a password string, calculate its strength, where strength is equals to the sum of count of distinct characters in all the substrings of that string.
Example: "aba" -> answer is 9
1st Approach:

At first I generated all substrings in 2 for loops, but instead of string, I had a SET of characters.
For each larger length created the SET from previous calculated SET
Size of the SET gave the distinct count and also the size of the SET will be a constant 26
Overall Time complexity wasO(26.N^2), but it was TLE in 2 test cases.
2nd Approach:

I tried the contribution approach, where I kept the track of contribution of individual character. (for each character at i, there can be i substrings ending there)
And also maintained the lastSeen position of the character
Once a duplicate character was encountered, subtracted the lastSeen Index.
Time - O(N)

Work Simulation

Approach/Design Questions mostly on a problem statement
Example: creating a voting app for a music competition, expecting million of users to vote within 5 minutes, and results to be displayed refreshes every second. There was given a choices of different data stores and had to rate them on best suitability
Some questions were more on how would you evaluate a particular approach, rate the criterias mentioned
Work Style Surveys

How you work in certain situations
More like a managerial round
"""