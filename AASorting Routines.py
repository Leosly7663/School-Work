import random


nums = [random.randrange(0, 1000, 1) for i in range(int(input("How many numbers do you want in the list?: ")))]


def selectionSort(nums):
    smallestNumber = 1

    # look through each index to find which number is the smallest

    def swap(currentIndex, smallest, switch):
        nums[switch] = nums[currentIndex]
        nums[currentIndex] = smallest

    for start in range(0, len(nums) - 1):
        smallestNumber = nums[start]
        temp = start
        for i in range(start, len(nums)):
            if nums[i] < smallestNumber:
                smallestNumber = nums[i]
                temp = i
        swap(start, smallestNumber, temp)
    return nums

def bubbleSort(nums):

    def swapBubble(i):
        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp

    for w in range(1, len(nums) - 1):
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                swapBubble(i)
    return nums


def insertionSort(nums):

    for i in range(1, len(nums)):
        pop = nums[i]
        currentIndex = i

        while (currentIndex > 0) and (nums[currentIndex - 1] > pop):
            nums[currentIndex] = nums[currentIndex - 1]
            currentIndex -= 1
        nums[currentIndex] = pop

    return nums

def quickSort(nums):

    def quick_sort(data, low, high):
        if low < high:
            partition_loc = partition(data, low, high)
            quick_sort(data, low, partition_loc - 1)
            quick_sort(data, partition_loc + 1, high)

    def partition(data2, left, right):
        move_left = True
        separator = data2[left]

        while left < right:
            if move_left == True:
                while (data2[right] >= separator) and (left < right):
                    right -= 1
                data2[left] = data2[right]
                move_left = False
            else:
                while (data2[left] <= separator) and (left < right):
                    left += 1
                data2[right] = data2[left]
                move_left = True
        data2[left] = separator
        return left
    quick_sort(nums, 0, len(nums) - 1)
    return nums


sortMethod = int(input(
'''What type of sorting method would you like to use?
1 - Selection sort
2 - Bubble sort
3 - Insertion sort
4 - Quick sort 
'''))

order = int(input(
'''What type of sorting method would you like to use?
1 - Ascending
2 - Descending
'''))

x = "null"
y = "null"
A = True
output = "null"

if sortMethod == 1:
    output = selectionSort(nums)
    x = "selection"
elif sortMethod == 2:
    output = bubbleSort(nums)
    x = "bubble"
elif sortMethod == 3:
    output = insertionSort(nums)
    x = "insertion"
elif sortMethod == 4:
    output = quickSort(nums)
    x = "quick"

if order == 1:
    A = True
    y = "ascending"
elif order == 2:
    A = False
    y = "descending"

print("Performing " + x + " sort in " + y + " order")


if A is True:
    print(output)
else:
    output.reverse()
    print(output)
