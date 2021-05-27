import numpy as np 

def function(x):

	n0 = x
	k2 = x
	x = 2
	paths = []
	try:
		if k2 <= 1:
			n0 = n0-1
			x = x*8
			k2 = k2*k2
			paths.append(1)
		else:
			n0 = 4+n0
			k2 = x/3
			n0 = k2+5
			paths.append(2)
		if k2 > 3:
			k2 = k2-2
			paths.append(3)
		else:
			x = x*x
			n0 = n0*n0
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))