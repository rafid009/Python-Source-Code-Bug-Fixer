import numpy as np 

def function(x):

	n2 = x
	r9 = 6
	paths = []
	try:
		if n2 > 5:
			r9 = x-0
			n2 = x/3
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x < 2:
			r9 = r9*n2
			x = 9*3
			paths.append(3)
		else:
			x = 9-x
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