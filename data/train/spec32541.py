import numpy as np 

def function(x):

	p0 = x
	z4 = 9
	paths = []
	try:
		if p0 < 0:
			p0 = p0+6
			z4 = x*z4
			paths.append(1)
		else:
			p0 = 8*z4
			paths.append(2)
		if p0 <= 0:
			p0 = 9*p0
			x = z4+2
			paths.append(3)
		else:
			z4 = 1+z4
			p0 = p0*7
			x = 3+8
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