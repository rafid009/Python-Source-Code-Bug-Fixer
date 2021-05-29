import numpy as np 

def function(x):

	r6 = x
	n5 = x
	paths = []
	try:
		if x <= 9:
			x = n5/x
			r6 = 1-x
			n5 = n5+n5
			paths.append(1)
		else:
			r6 = 8+r6
			n5 = n5-9
			n5 = 2*n5
			paths.append(2)
		if n5 < 6:
			x = n5+6
			paths.append(3)
		else:
			n5 = n5+3
			x = x+n5
			r6 = 9/n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))