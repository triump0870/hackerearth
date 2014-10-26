def checkDivisibility(number, val):
# Strip all powers of subsequent primes from the number	till the number equal to the prime which divides it
	i = 1;
	factors = []
	while(number%val == 0):
		#print number, val**i;
		factors.append(val**i);
		number = number / val; # Reduce the number by factor of val
		i = i + 1;
	return (number, factors)
def updateFactors(factors, factor):
	# Function to update the factors of the number with the factors found using checkDivisibility
	if factor != [] :
	# Append factor only if it is non empty
		factors.append(factor);
	return factors
def nextprime(loop, current_index, prime_list):
# Function to return the next prime to check for and also to populate the list array with numbers mapping to the current list items for the next 30 numbers.
	if(current_index == 7):
		loop = loop+1;
		current_index = 0;
	else:
		current_index = current_index +1
	return (loop * 30 + prime_list[current_index], loop, current_index, prime_list)
 
def findFactors(number):
	# Function to find all the factors of the number and to also print the largest factor of the number
	val = 7;
	loop = 0;
	current_index = 1;
	prime_list = [1,7,11,13,17,19,23,29]; # List to populate with all primes less than 30
 
	factors = []; # Store all prime powers of a number
	# Strip all powers of 2 from the number	
	number, factor = checkDivisibility(number, 2);
	factors = updateFactors(factors, factor);
 
	# Strip all powers of 3 from the number
	number, factor = checkDivisibility(number, 3);
	factors = updateFactors(factors, factor);
 
	# Strip all powers of 5 from the number
	number, factor = checkDivisibility(number, 5);
	factors = updateFactors(factors, factor);	
 
	# Strip all powers of subsequent primes from the number	till the number equal to the prime which divides it
	while(number/val != 0):
		number, factor = checkDivisibility(number, val);
		factors = updateFactors(factors, factor);
		#Get Next Prime to check for and simultaneously update loop, current_index and prime_list
		val, loop, current_index, prime_list = nextprime(loop, current_index, prime_list)
	#Append the last factor in the factor list
	#factors.append([val])
	#print "Largest Prime:", factors[-1][0]
	return factors;
t =input()
for i in xrange(t):
	r = input()
	a = min(findFactors(r)[0])
	b = r-a
	print b