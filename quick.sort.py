print("array Sorting and Elenment Replacement")

arr = input("Enter the array elemens separated by the spaces: ")
arr = list(map(int,arr.split()))

def sort_arr(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = [x for x in array[:-1] if x <= pivot]
    right = [x for x in array[:-1] if x > pivot]

    return sort_arr(left) + [pivot] + sort_arr(right)

print(f"Array: {arr}")
print(f"sorted array using quick serch: {sort_arr(arr)}")

def search_element_and_replace(array, target, replacement):
    if target not in array:
        return "Element not found in given array"

    for i in array:
        if i == target:
            array.remove(i)
            array.append(replacement)
    return f"Modified Array after replacing {target} with {replacement} : {sort_arr(array)}"

target = int(input("Enter element to search: "))
replacement = int(input("Enter element to replace: "))
searched = search_element_and_replace(sort_arr(arr), target, replacement)
print(searched)