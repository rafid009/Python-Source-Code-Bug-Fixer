import numpy as np 

def function(x):

	o4 = x
	p4 = x
	paths = []
	try:
		if o4 < 2:
			o4 = o4+4
			x = x*5
			paths.append(1)
		else:
			o4 = 5+o4
			paths.append(2)
		if x > 0:
			p4 = o4+p4
			x = p4*x
			paths.append(3)
		else:
			o4 = 3+o4
			p4 = x*p4
			o4 = x+o4
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