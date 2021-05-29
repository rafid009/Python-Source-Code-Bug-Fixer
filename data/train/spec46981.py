import numpy as np 

def function(x):

	z1 = 8
	p2 = 6
	paths = []
	try:
		if x < 7:
			x = 8+x
			z1 = 8+0
			x = x*3
			paths.append(1)
		else:
			p2 = 2-p2
			paths.append(2)
		if z1 <= 2:
			p2 = p2-4
			p2 = p2/z1
			p2 = p2/9
			paths.append(3)
		else:
			p2 = 6+p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))