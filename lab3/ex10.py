#Remove Duplicates from List
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result