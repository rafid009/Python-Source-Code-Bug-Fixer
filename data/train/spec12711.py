import numpy as np 

def function(x):

	z5 = x
	p6 = 8
	paths = []
	try:
		if p6 > 6:
			x = 0+x
			z5 = 6/z5
			paths.append(1)
		else:
			x = x*5
			x = 1-x
			z5 = 5-7
			paths.append(2)
		if p6 < 4:
			p6 = 4-p6
			x = x+p6
			p6 = z5-p6
			paths.append(3)
		else:
			p6 = 5+x
			p6 = p6/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))