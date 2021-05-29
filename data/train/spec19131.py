import numpy as np 

def function(x):

	x2 = 5
	v3 = x
	paths = []
	try:
		if v3 < 0:
			x = 6+x
			x = v3*x
			paths.append(1)
		else:
			v3 = v3/8
			v3 = v3-7
			paths.append(2)
		if x2 < 5:
			x2 = x2-4
			paths.append(3)
		else:
			x = 4+x
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