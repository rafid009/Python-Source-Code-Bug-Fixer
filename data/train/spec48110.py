import numpy as np 

def function(x):

	p3 = 6
	e3 = x
	paths = []
	try:
		if e3 < 7:
			x = 8*8
			x = x+2
			x = 2/7
			paths.append(1)
		else:
			x = 7-x
			p3 = 8/p3
			x = 5*x
			paths.append(2)
		if e3 > 4:
			e3 = e3/7
			x = 8*x
			paths.append(3)
		else:
			p3 = x+2
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