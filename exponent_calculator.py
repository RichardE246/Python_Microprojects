#This program takes two numbers, a base, n and a question number, x.
#It then determines whether x is actually an exponential number (e.g. 4 is 2^2) of n.
#If so, what power is it.


n = 0 #base number
x = 0 #exponential number

print(" Program to determine whether a number is an exponential number, given a base")
while(1):
	cnt = 0
	n = input(" input base: ")
	x = float(input(" input ques number: "))
	while(x > 1): 
		x = x/int(n) #divide exp number by base until it reaches 1
		cnt = cnt + 1 #increment counter, this is the "power of"
	if (x == 1):
		print(" num is an exponent of "+ str(n) + ":  " + "^" + str(cnt))
	elif (x < 1):
		print (" num is not an exponent of base") #if it dips below 1 it is not an exponential number
	
	
