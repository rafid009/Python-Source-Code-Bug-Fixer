import numpy as np 

def function(x):

	e4 = x
	p4 = 8
	paths = []
	try:
		if p4 < 6:
			p4 = 6/p4
			paths.append(1)
		else:
			x = x+x
			x = p4-x
			paths.append(2)
		if e4 >= 7:
			x = x-9
			paths.append(3)
		else:
			p4 = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))