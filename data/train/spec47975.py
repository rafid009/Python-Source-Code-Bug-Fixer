import numpy as np 

def function(x):

	n3 = x
	r4 = x
	paths = []
	try:
		if r4 >= 8:
			x = x*r4
			paths.append(1)
		else:
			x = 0+9
			n3 = x+n3
			paths.append(2)
		if r4 < 0:
			x = 4*r4
			n3 = 7/r4
			paths.append(3)
		else:
			n3 = 1-n3
			n3 = n3/3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))