import numpy as np 

def function(x):

	p5 = 1
	z2 = x
	x = x
	paths = []
	try:
		if x < 1:
			z2 = z2/z2
			paths.append(1)
		else:
			p5 = z2/9
			paths.append(2)
		if x >= 1:
			p5 = p5-9
			x = z2*7
			paths.append(3)
		else:
			z2 = z2*z2
			x = x/8
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