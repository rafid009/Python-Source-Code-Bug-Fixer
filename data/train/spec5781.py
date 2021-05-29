import numpy as np 

def function(x):

	p3 = 6
	z7 = x
	paths = []
	try:
		if p3 >= 0:
			x = x-8
			p3 = p3+p3
			paths.append(1)
		else:
			z7 = 9/z7
			paths.append(2)
		if x >= 1:
			x = 7+3
			p3 = z7*8
			z7 = 6*z7
			paths.append(3)
		else:
			z7 = 5+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))