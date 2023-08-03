# Longest Substring Without Repeating Characters

This is a Python script that reads a string from the command line and finds the longest substring in it that doesn't contain any duplicate characters. 
If there are multiple substrings of equal length that satisfy the condition,
returning any of these substrings would be a valid answer.

## Usage

1. Make sure to you have Python on your system.
2. Open a terminal or command prompt in the directory where the `question.py` script is located.
3. Run the command: $ python3 question.py
4. Enter the string from the console.

## Input Format

The first line contains a single string of input, **input**.

## Output Format

The output should be displayed after **output:**, including
**length:

Example 1:

$ python3 solution.py
input: ABBCDDEFGHII
output: DEFGHI length: 6

Example 2:

$ python3 solution.py
input: AABBCCD
output: AB length: 2
output: BC length: 2
output: CD length: 2
<any of the above 3 would be accepted>

Example 3:

$ python3 solution.py
input: ABCD
output: ABCD length: 4

Time Complexity=O(n)