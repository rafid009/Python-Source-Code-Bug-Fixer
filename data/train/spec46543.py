import numpy as np 

def function(x):

	p3 = x
	x7 = 6
	paths = []
	try:
		if p3 >= 1:
			x = 3*x7
			p3 = p3*x7
			p3 = p3*9
			paths.append(1)
		else:
			p3 = p3-x
			paths.append(2)
		if p3 < 8:
			p3 = x7*8
			paths.append(3)
		else:
			x7 = 2/x7
			x7 = x7-5
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