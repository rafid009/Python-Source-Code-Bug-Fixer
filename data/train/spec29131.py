import numpy as np 

def function(x):

	p7 = x
	z9 = 8
	x = 7
	paths = []
	try:
		if p7 < 8:
			z9 = 9/p7
			z9 = z9/3
			paths.append(1)
		else:
			z9 = z9*7
			x = x-z9
			p7 = 6*z9
			paths.append(2)
		if z9 >= 8:
			p7 = p7+8
			paths.append(3)
		else:
			p7 = 7/p7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		p7 = z9**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))