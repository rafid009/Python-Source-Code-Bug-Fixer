import numpy as np 

def function(x):

	n3 = x
	j4 = 0
	paths = []
	try:
		if j4 > 3:
			n3 = n3+j4
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x <= 6:
			n3 = 3+n3
			n3 = x*n3
			paths.append(3)
		else:
			n3 = 3-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))