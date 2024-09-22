
list=[] 

for i in range (1,11):
 list+=[i]
print("---------------------------------")
print ("Print a list")

for i in list:
	print(i	 ,end="")
print("\n\n")
print("---------------------------------")
print("\n\n")
print   ("Index,Value")
for i in range (len(list)):
	print("%d      %d"%(i,list[i]))
print("---------------------------------")
print("\n\n")
print ("Change  a list element ") 
list[0]=123 
print("---------------------------------")
print("\n\n")
print ("Print a list after changing an element ")
print   ("Index,Value")
for i in range (len(list)):
	print("%d      %d"%(i,list[i]))

