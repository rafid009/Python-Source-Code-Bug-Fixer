import numpy as np 

def function(x):

	z1 = 5
	p2 = x
	paths = []
	try:
		if z1 > 9:
			p2 = p2+6
			x = x+9
			paths.append(1)
		else:
			x = x-4
			x = x+z1
			p2 = p2-4
			paths.append(2)
		if x < 8:
			z1 = 6*1
			paths.append(3)
		else:
			p2 = p2+7
			z1 = 1*5
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		z1 = p2**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))