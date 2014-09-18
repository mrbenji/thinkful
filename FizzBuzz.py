
limit = 100

def fizzBuzz(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return "fizz buzz"
        else: return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else: return num

print "Fizz buzz counting up to %s" % str(limit)
buzzmod = [fizzBuzz(i) for i in range(1,limit+1)]
for x in buzzmod: print x
