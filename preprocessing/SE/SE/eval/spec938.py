import numpy as np 

def function(x):

	v4 = x
	p6 = 4
	paths = []
	try:
		if v4 <= 0:
			x = 8*6
			v4 = v4-v4
			x = 1-3
			paths.append(1)
		else:
			v4 = 4/v4
			p6 = v4/x
			x = 0-x
			paths.append(2)
		if x < 5:
			p6 = p6+0
			paths.append(3)
		else:
			x = p6*x
			x = 1/6
			v4 = v4-4
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