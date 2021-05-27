import numpy as np 

def function(x):

	p8 = x
	z2 = x
	paths = []
	try:
		if x > 0:
			x = x/9
			paths.append(1)
		else:
			z2 = z2-0
			z2 = z2/2
			p8 = 1+3
			paths.append(2)
		if p8 <= 6:
			x = 7/4
			x = x-7
			paths.append(3)
		else:
			p8 = 0*1
			x = x+3
			p8 = 1/5
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