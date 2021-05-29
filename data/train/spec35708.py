import numpy as np 

def function(x):

	r4 = 6
	n6 = x
	paths = []
	try:
		if r4 <= 2:
			x = 0-x
			paths.append(1)
		else:
			n6 = 3+n6
			paths.append(2)
		if r4 >= 2:
			x = x*2
			paths.append(3)
		else:
			r4 = r4+n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))