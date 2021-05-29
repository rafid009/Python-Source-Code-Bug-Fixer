import numpy as np 

def function(x):

	n0 = 9
	v6 = 6
	paths = []
	try:
		if n0 <= 8:
			v6 = v6+n0
			paths.append(1)
		else:
			n0 = 5*x
			paths.append(2)
		if n0 > 2:
			x = v6-v6
			x = 5*3
			n0 = v6+x
			paths.append(3)
		else:
			v6 = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))