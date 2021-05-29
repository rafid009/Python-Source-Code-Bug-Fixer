import numpy as np 

def function(x):

	n9 = 7
	q2 = x
	paths = []
	try:
		if q2 < 3:
			x = x+9
			x = x-1
			paths.append(1)
		else:
			n9 = n9+n9
			paths.append(2)
		if x >= 2:
			x = x+n9
			x = x/8
			x = 3*n9
			paths.append(3)
		else:
			n9 = 1+9
			n9 = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))