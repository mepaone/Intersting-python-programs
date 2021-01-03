#Program for printing the last two characters of a string

# example:  string="apple"
#           apple --> l e ---->e l(output)


string=input("enter any string: ")

lenght=len(string)            #the above line is used to fing the lenght of string.
                              # if string is "Apple",Then the lenght will be 5

first=string[lenght-1]        #this line subtracts the total string lengh by 1 and provides the first last character.

second=string[lenght-2]       #this line subtracts the total string lengh by 1 and provides the second last character.

print(first,second,end="")    #(end="") is used to provide space between the first and second variables.
