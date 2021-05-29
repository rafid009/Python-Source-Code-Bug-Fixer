import numpy as np 

def function(x):

	t6 = x
	n0 = x
	paths = []
	try:
		if t6 >= 4:
			x = 4*x
			n0 = 4+x
			n0 = 5/n0
			paths.append(1)
		else:
			x = 3-6
			n0 = t6/n0
			paths.append(2)
		if t6 < 4:
			n0 = n0/5
			n0 = n0*6
			paths.append(3)
		else:
			n0 = n0-5
			x = 6*6
			n0 = n0+n0
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		n0 = t6**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))