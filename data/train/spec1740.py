import numpy as np 

def function(x):

	v9 = x
	p6 = x
	x = x
	paths = []
	try:
		if v9 < 8:
			x = 9+x
			x = 9-x
			p6 = 9+p6
			paths.append(1)
		else:
			p6 = p6+p6
			x = 3-x
			paths.append(2)
		if v9 < 3:
			p6 = p6-x
			x = p6*x
			x = p6/x
			paths.append(3)
		else:
			p6 = 5-0
			x = 2*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))