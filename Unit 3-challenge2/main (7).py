#3.2 Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

print("-----Program for printing student name with marks using list-----") 
  
# create an empty dictionary 
D = {} 
  
n = int(input('How many student record you want to store?? ')) 
  
# create an empty list 
# Add student information to the list 
ls = [] 
  
for _i in range(0, n): 
    
      # Take combined input name and  
    # percentage and split values  
    # using split function. 
    x,y = input("Enter the student name and it's percentage: ").split() 
      
    # Add name and marks stored in x, y 
    # respectively using tuple to the list 
    ls.append((y,x)) 
      
# sort the elements of list 
# based on marks 
ls = sorted(ls, reverse = True) 
  
print('Sorted list of students according to their marks in descending order') 
  
for i in ls: 
    
    # print name and marks stored in  
    # second and first position  
    # respectively in list of tuples. 
    print(i[1], i[0])