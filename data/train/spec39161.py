import numpy as np 

def function(x):

	p4 = 3
	z5 = x
	paths = []
	try:
		if x > 5:
			p4 = p4/p4
			x = 9-8
			p4 = 9+p4
			paths.append(1)
		else:
			z5 = z5-9
			z5 = x/5
			paths.append(2)
		if p4 > 4:
			p4 = z5*p4
			p4 = 6/p4
			paths.append(3)
		else:
			z5 = z5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))