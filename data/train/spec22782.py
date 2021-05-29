import numpy as np 

def function(x):

	b0 = x
	z1 = x
	paths = []
	try:
		if z1 < 2:
			x = x+2
			b0 = z1*2
			paths.append(1)
		else:
			z1 = z1*1
			paths.append(2)
		if b0 > 4:
			z1 = 2-6
			b0 = 6*6
			b0 = 7+3
			paths.append(3)
		else:
			x = 1*x
			x = x/1
			b0 = 0*2
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