import numpy as np 

def function(x):

	p7 = 3
	z2 = 8
	paths = []
	try:
		if z2 >= 9:
			x = p7/8
			paths.append(1)
		else:
			z2 = z2+9
			x = x+0
			x = 4/x
			paths.append(2)
		if z2 <= 9:
			x = 5*7
			paths.append(3)
		else:
			z2 = z2/7
			x = x+7
			p7 = x-p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		z2 = p7**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))