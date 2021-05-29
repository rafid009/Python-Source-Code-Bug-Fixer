import numpy as np 

def function(x):

	n0 = x
	a0 = x
	paths = []
	try:
		if x < 6:
			x = a0+9
			a0 = 0/n0
			a0 = a0/n0
			paths.append(1)
		else:
			n0 = 2-n0
			paths.append(2)
		if a0 >= 0:
			x = a0*x
			x = 0+x
			a0 = 2*a0
			paths.append(3)
		else:
			a0 = 9+a0
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