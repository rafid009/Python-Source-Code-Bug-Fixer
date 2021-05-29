import numpy as np 

def function(x):

	p3 = 4
	e8 = 7
	paths = []
	try:
		if x <= 7:
			p3 = p3*4
			p3 = 3/e8
			paths.append(1)
		else:
			p3 = p3/x
			x = x+8
			paths.append(2)
		if e8 > 3:
			p3 = x*x
			p3 = e8/p3
			paths.append(3)
		else:
			p3 = e8-2
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