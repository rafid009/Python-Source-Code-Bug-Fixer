import numpy as np 

def function(x):

	p9 = 6
	x2 = 4
	paths = []
	try:
		if x2 <= 3:
			x2 = 7/p9
			p9 = 0*p9
			p9 = p9-3
			paths.append(1)
		else:
			x2 = 1-x2
			paths.append(2)
		if x <= 2:
			x = x/8
			paths.append(3)
		else:
			x = x2-x
			x2 = 3/9
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