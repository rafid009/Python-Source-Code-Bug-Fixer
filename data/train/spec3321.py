import numpy as np 

def function(x):

	p0 = x
	f0 = x
	paths = []
	try:
		if p0 >= 1:
			p0 = 0+p0
			p0 = p0/f0
			paths.append(1)
		else:
			p0 = 9-f0
			paths.append(2)
		if p0 > 1:
			p0 = p0/p0
			paths.append(3)
		else:
			x = 6+p0
			x = f0*x
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