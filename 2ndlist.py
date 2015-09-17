# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
nums = raw_input()
ls = map(int, nums.split())
largest = ls[0]
second = -101
for i in range(1, n):
    if ls[i] > largest:
        largest = ls[i]

for i in range(1, n):
    if ls[i] < largest:
        if ls[i] > second:
            second = ls[i]
print second