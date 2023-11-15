#find the largest number
def find_largest_no(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1
    return arr[0]  
#Open th file, call the find_largest_no() and print result
def main():
    with open("find_largest_number_input.txt", "r") as file:
        for line in file:
            array = [int(num) for num in line.strip().split(',')]
            print(f"Array: {', '.join(map(str, array))}")
            max_number = find_largest_no(array)
            print(f"Max:{max_number}")
            print()

if __name__ == "__main__":
    main()
