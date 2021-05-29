import numpy as np 

def function(x):

	f0 = x
	p0 = 4
	x = x
	paths = []
	try:
		if p0 > 6:
			p0 = p0*6
			x = p0*x
			p0 = x-p0
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if p0 > 3:
			p0 = p0*8
			f0 = f0/x
			f0 = f0+9
			paths.append(3)
		else:
			f0 = 4+f0
			x = x*x
			p0 = 8+5
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