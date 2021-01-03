#Program for printing the number of parentheses required for balancing the given input
#Example:     if input= ())
#            Then we have to add one "(" on the left to balance the input
#             i.e, ()) ---> (())
#             hence the output will be 1, since only one parentheses is added

#s=input("enter the parentheses pattern: ")
s="()))"
p="("
q=")"
count=0
c=0
for i in s:
#For loop is used for seperating the entered "s" values
#example:if s=()) then i= ( , ) , )
    if i==p:
        #checks weather the i value is equal to "("
        count+=1
    elif i==q:
        #checks weather the i value is equal to ")"
        c+=1
if count!=c:
    if count>c:
        count=count-c
    elif count<c:
        count=c-count
    else:
        count=0
print(count)
#prints the final count value after completing the "for" loop for obtained i values.
#If we get 3 "i" values then the loop is exected 3 times and final count value is count is printed.
