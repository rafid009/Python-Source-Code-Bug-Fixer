import numpy as np 

def function(x):

	l3 = x
	n0 = x
	paths = []
	try:
		if l3 <= 1:
			l3 = x/l3
			l3 = 0*n0
			n0 = n0*5
			paths.append(1)
		else:
			l3 = 0-x
			n0 = 8+l3
			paths.append(2)
		if l3 > 2:
			n0 = 6*n0
			l3 = l3+x
			paths.append(3)
		else:
			n0 = n0-x
			l3 = n0-6
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