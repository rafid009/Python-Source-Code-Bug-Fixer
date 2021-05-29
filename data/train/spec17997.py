import numpy as np 

def function(x):

	n0 = 4
	r7 = x
	paths = []
	try:
		if x >= 3:
			n0 = n0+x
			n0 = 6-n0
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x > 6:
			n0 = n0-4
			n0 = 1*n0
			x = 3+x
			paths.append(3)
		else:
			n0 = n0-7
			r7 = 6-6
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))