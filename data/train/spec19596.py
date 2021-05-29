import numpy as np 

def function(x):

	p8 = 6
	e4 = x
	paths = []
	try:
		if p8 < 3:
			x = 3/7
			p8 = p8*6
			e4 = 0*2
			paths.append(1)
		else:
			e4 = e4*7
			paths.append(2)
		if e4 < 9:
			x = 6/x
			e4 = 2/5
			x = 1*x
			paths.append(3)
		else:
			e4 = 5+e4
			x = 5/7
			e4 = 3+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))