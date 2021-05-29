import numpy as np 

def function(x):

	o4 = x
	p1 = x
	paths = []
	try:
		if o4 > 8:
			x = x*4
			p1 = 6*x
			paths.append(1)
		else:
			p1 = o4/7
			paths.append(2)
		if x <= 0:
			p1 = p1-7
			p1 = x*7
			paths.append(3)
		else:
			x = 6/x
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