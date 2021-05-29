import numpy as np 

def function(x):

	o5 = 2
	p0 = x
	paths = []
	try:
		if o5 < 2:
			x = 5/6
			p0 = p0-5
			paths.append(1)
		else:
			o5 = 1-o5
			paths.append(2)
		if o5 < 3:
			o5 = 3/1
			paths.append(3)
		else:
			o5 = o5/o5
			p0 = p0-5
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