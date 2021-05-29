import numpy as np 

def function(x):

	n4 = x
	n0 = x
	paths = []
	try:
		if x >= 8:
			n4 = x/2
			n4 = n4/6
			n4 = 6+x
			paths.append(1)
		else:
			n0 = n0/7
			n0 = 2/5
			paths.append(2)
		if n4 < 2:
			x = 8/x
			n4 = 1*n4
			paths.append(3)
		else:
			x = x/4
			n4 = n4+x
			x = 0/4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n0 = n4**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))