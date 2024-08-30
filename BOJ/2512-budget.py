import sys

input = sys.stdin.readline

N = int(input())
budgetArray = list(map(int, input().split()))
totalBudget = int(input())

start = 0
end = 0

start = int(totalBudget / N)
end = max(budgetArray)

while start <= end:
    mid = int((start + end) / 2)
    budgetSum = 0
    for budget in budgetArray:
        if budget > mid:
            budgetSum += mid
        else:
            budgetSum += budget
    if budgetSum > totalBudget:
        end = mid - 1
    else:
        start = mid + 1

print(end)