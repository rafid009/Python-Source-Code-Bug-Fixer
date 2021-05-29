import numpy as np 

def function(x):

	n6 = 5
	x0 = x
	x = x
	paths = []
	try:
		if n6 > 5:
			x0 = x+2
			n6 = n6-6
			n6 = 2/n6
			paths.append(1)
		else:
			n6 = n6-2
			n6 = x0+n6
			paths.append(2)
		if x0 >= 9:
			n6 = x*8
			x0 = 5*x0
			n6 = n6/x0
			paths.append(3)
		else:
			n6 = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))