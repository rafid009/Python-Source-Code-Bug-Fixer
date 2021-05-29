import numpy as np 

def function(x):

	o0 = x
	p0 = 8
	paths = []
	try:
		if p0 > 7:
			p0 = 8*6
			p0 = 6-3
			o0 = o0+4
			paths.append(1)
		else:
			x = o0-x
			paths.append(2)
		if p0 >= 3:
			o0 = p0+o0
			p0 = p0*3
			p0 = x-p0
			paths.append(3)
		else:
			p0 = p0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))