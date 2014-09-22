
limit = 100

def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    if num % 3 == 0:
    	return "fizz"
    if num % 5 == 0:
        return "buzz"
    return num

print "Fizz buzz counting up to %s" % str(limit)
for i in range(limit):
	print fizzBuzz(i+1)