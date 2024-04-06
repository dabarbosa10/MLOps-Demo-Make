def binary_search(ordered_list, search_value):
    first=0
    last=len(ordered_list)-1

    while first<=last:
        middle=(last+first)//2
        print(f'This is the middle: {middle}')
        if search_value==ordered_list[middle]:
            return True, search_value
        elif search_value<ordered_list[middle]:
            last=middle-1
        else:
            first=middle+1
    return False, search_value


def binary_search_recursive(ordered_list, search_value):
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return binary_search_recursive(ordered_list[middle+1:],search_value)
  
print(binary_search_recursive([1,5,8,9,15,20,70,72],11))

print(binary_search([1,5,8,9,15,20,70,72], 11))