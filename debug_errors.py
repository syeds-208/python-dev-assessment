def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Returns None if the list is empty.
    """
    total = 0
    try:
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)
    except ZeroDivisionError:
        return None


data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

def get_list_element(my_list, index):
    """
    Returns the element at the specified index in a list.
    Handles IndexError and TypeError.
    Returns None if an error occurs.
    """
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")
        return None
    except TypeError:
        print("Error: Invalid index type. Please provide an integer.")
        return None    

print(get_list_element([1, 2, 3], 1))      # Output: 2
print(get_list_element([1, 2, 3], 10))     # Error message + None
print(get_list_element("hello", 2))        # Error message + None
