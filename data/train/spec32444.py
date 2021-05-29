import numpy as np 

def function(x):

	b2 = 0
	n1 = 1
	paths = []
	try:
		if b2 >= 4:
			b2 = b2+7
			x = x/2
			b2 = 6-n1
			paths.append(1)
		else:
			b2 = x/4
			b2 = x*b2
			n1 = n1-5
			paths.append(2)
		if x > 8:
			n1 = x-5
			paths.append(3)
		else:
			x = x+1
			b2 = 9+x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		n1 = b2**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))