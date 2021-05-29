import numpy as np 

def function(x):

	e0 = 2
	p2 = 0
	paths = []
	try:
		if p2 > 2:
			x = x*7
			x = 2+3
			paths.append(1)
		else:
			x = 0-2
			paths.append(2)
		if x >= 4:
			x = x+7
			paths.append(3)
		else:
			x = e0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))