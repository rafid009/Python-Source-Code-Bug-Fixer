import numpy as np 

def function(x):

	p2 = 2
	z5 = 1
	paths = []
	try:
		if p2 >= 2:
			p2 = 4*p2
			p2 = p2-9
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x > 6:
			z5 = z5-7
			paths.append(3)
		else:
			p2 = p2*4
			x = x-3
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		p2 = z5**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))