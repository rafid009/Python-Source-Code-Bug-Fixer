import numpy as np 

def function(x):

	p0 = 7
	o4 = 5
	paths = []
	try:
		if x <= 2:
			o4 = o4/6
			o4 = x/o4
			paths.append(1)
		else:
			o4 = p0-o4
			x = 0*2
			x = x*1
			paths.append(2)
		if x > 8:
			p0 = 7/8
			p0 = p0/2
			paths.append(3)
		else:
			p0 = p0-5
			x = x-2
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))