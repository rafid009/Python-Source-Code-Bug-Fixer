import numpy as np 

def function(x):

	p3 = 9
	e6 = x
	x = x
	paths = []
	try:
		if e6 < 5:
			p3 = x+8
			paths.append(1)
		else:
			e6 = 7+e6
			p3 = 0/p3
			p3 = 0+e6
			paths.append(2)
		if x > 6:
			p3 = p3-x
			e6 = e6-x
			p3 = 6/p3
			paths.append(3)
		else:
			p3 = 0/p3
			x = p3-x
			e6 = e6*3
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