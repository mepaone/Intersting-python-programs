"""
-Alice owns a company that transports tour groups between two islands.

-She has n trips booked, and each trip has pi passengers. Alice has m boats for transporting people,
 and each boat's maximum capacity is c passengers.

-Given the number of passengers going on each trip,
-determine whether or not Alice can perform all n trips using no more than m boats per individual trip.

-If this is possible, print Yes; otherwise, print No."""


n,c,m=(map(int,input().split()))      #This line is used to take input values of n.o of trips(n),capacity per boat(c),n.o of boats(m).

pi=(map(int,input().split()))         #This line is used to take the number of passenges per trip in a list.

count=0
for i in pi:                          #the n.o of list passengers are separated into individual digits.

    if count<=i:                      #for each digit it checks weather "i" value is greater than the count value.
        count=i
    else:                             #if count is greater then the same value is returned in count.
        count=count
if m*c>=count:                        #the count variable consists of max number of passengers among the entered list and compared them with m*c.
    print("yes")
else:                                 #If the value of m*c is lesser the the count value then the output is No.
    print("No")