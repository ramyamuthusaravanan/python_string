#Write a Python program to accept the user's first and last name and then getting them printed 
#in the the reverse order with a space between first name and last name. 
FirstName=(input("Enter the First Name : "))         
LastName=(input("\nEnter the Last Name : "))
print(FirstName[::-1]+" "+LastName[::-1])