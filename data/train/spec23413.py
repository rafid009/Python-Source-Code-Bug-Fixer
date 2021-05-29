import numpy as np 

def function(x):

	p0 = x
	z2 = 8
	paths = []
	try:
		if x >= 0:
			x = 8/p0
			x = x/5
			p0 = p0+2
			paths.append(1)
		else:
			z2 = 6+z2
			x = 3+x
			paths.append(2)
		if z2 <= 9:
			p0 = p0+3
			p0 = z2/p0
			paths.append(3)
		else:
			p0 = z2-9
			p0 = 3-z2
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))