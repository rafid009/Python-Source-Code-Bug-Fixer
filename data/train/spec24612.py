import numpy as np 

def function(x):

	u4 = x
	n0 = x
	paths = []
	try:
		if u4 >= 5:
			x = x+3
			n0 = n0*2
			paths.append(1)
		else:
			u4 = u4*n0
			paths.append(2)
		if n0 >= 6:
			n0 = n0-8
			u4 = 2*u4
			x = x*x
			paths.append(3)
		else:
			u4 = 9+u4
			n0 = n0*3
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