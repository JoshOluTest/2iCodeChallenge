def count_pairs_with_sum(array, X):
    # This Initialize variables
    count = 0
    left = 0
    right = len(array) - 1

    # Loop through the array to find pairs
    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == X:
            count += 1
            left += 1
            right -= 1
        elif current_sum < X:
            left += 1
        else:
            right -= 1

    return count

# This get user input and X
try:
    input_array = input("Enter a sorted array of whole numbers (comma-separated): ")
    array = [int(num) for num in input_array.split(',')]
    X = int(input("Enter the integer X: "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    exit()


result = count_pairs_with_sum(array, X)
print(f"Number of pairs with sum {X}: {result}")
