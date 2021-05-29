import numpy as np 

def function(x):

	n9 = x
	z1 = 4
	paths = []
	try:
		if x < 3:
			n9 = x+x
			paths.append(1)
		else:
			x = x+7
			n9 = n9-2
			x = x/3
			paths.append(2)
		if z1 <= 8:
			x = x*6
			paths.append(3)
		else:
			z1 = 7*z1
			n9 = 4+5
			z1 = z1*2
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