import numpy as np 

def function(x):

	e1 = 8
	p1 = 6
	x = x
	paths = []
	try:
		if x < 8:
			e1 = e1+8
			p1 = 2-x
			paths.append(1)
		else:
			e1 = e1*p1
			x = e1-2
			e1 = 7-e1
			paths.append(2)
		if p1 < 0:
			e1 = e1/2
			paths.append(3)
		else:
			p1 = p1-3
			e1 = e1/2
			x = p1-e1
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