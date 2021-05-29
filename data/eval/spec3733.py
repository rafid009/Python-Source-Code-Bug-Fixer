import numpy as np 

def function(x):

	n2 = 3
	r4 = 7
	paths = []
	try:
		if x >= 6:
			r4 = r4/3
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if x >= 4:
			n2 = 0/4
			r4 = r4/9
			paths.append(3)
		else:
			n2 = 3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))