import numpy as np 

def function(x):

	p2 = x
	z2 = 2
	paths = []
	try:
		if x < 1:
			p2 = p2/9
			p2 = 6+7
			p2 = p2*p2
			paths.append(1)
		else:
			z2 = p2+2
			paths.append(2)
		if x >= 3:
			p2 = 4+p2
			p2 = p2*p2
			z2 = p2+z2
			paths.append(3)
		else:
			x = x+x
			p2 = p2*4
			p2 = p2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))