num, sum = 12345, 0


def findSum(num, sum):
    if num == 0:
        return sum

    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)


print(findSum(num, sum))

#OR

num, sum = 12345, 0

for i in range(len(str(num))):
    # ord methods helps with ASCII
    sum += ord(str(num)[i]) - 48

print(sum)
