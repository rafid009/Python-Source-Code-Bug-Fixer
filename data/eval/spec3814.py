import numpy as np 

def function(x):

	n0 = 7
	r4 = x
	paths = []
	try:
		if r4 < 6:
			r4 = r4-0
			paths.append(1)
		else:
			x = n0+x
			paths.append(2)
		if r4 <= 9:
			n0 = 3-n0
			paths.append(3)
		else:
			r4 = 3-6
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