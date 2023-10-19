#3.1 Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.

#Search function with parameter list name 
#and the value to be searched 


def search(List, n): 

    return any(List[i] == n for i in range(len(List)))


# list which contains both string and numbers. 
List = [1, 2, 'sachin', 4, 'Geeks', 6] 

# Driver Code 
n = 'Geeks'

if search(List, n): 
    print("Found") 
else: 
    print("Not Found")