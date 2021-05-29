import numpy as np 

def function(x):

	p0 = 0
	p3 = 8
	paths = []
	try:
		if p0 > 6:
			p3 = p3+3
			x = 3*x
			p3 = p3+4
			paths.append(1)
		else:
			x = 8+x
			p0 = 9+p0
			paths.append(2)
		if p3 > 6:
			p0 = 1/3
			p0 = x-5
			paths.append(3)
		else:
			p3 = p3*p0
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		p0 = p0**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))