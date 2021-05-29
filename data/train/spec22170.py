import numpy as np 

def function(x):

	n5 = x
	z4 = x
	paths = []
	try:
		if x > 4:
			n5 = 1+5
			paths.append(1)
		else:
			x = x*5
			n5 = n5-0
			n5 = x+x
			paths.append(2)
		if z4 <= 0:
			x = 0/x
			n5 = n5*n5
			paths.append(3)
		else:
			n5 = 5/4
			n5 = n5+3
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))