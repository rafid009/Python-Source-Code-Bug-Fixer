import numpy as np 

def function(x):

	z6 = x
	p0 = 1
	x = 7
	paths = []
	try:
		if x > 1:
			p0 = 8*p0
			paths.append(1)
		else:
			x = x*2
			x = 1*z6
			x = x+2
			paths.append(2)
		if z6 > 4:
			z6 = x/6
			x = x-8
			paths.append(3)
		else:
			p0 = 4/p0
			p0 = 4-p0
			x = 0*8
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