import numpy as np 

def function(x):

	n0 = 9
	i4 = x
	paths = []
	try:
		if i4 <= 8:
			x = x*7
			x = n0/x
			i4 = 8*x
			paths.append(1)
		else:
			n0 = 5-n0
			paths.append(2)
		if x > 4:
			i4 = 3-0
			n0 = 5*n0
			x = 2-n0
			paths.append(3)
		else:
			x = x*6
			n0 = 1-8
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))