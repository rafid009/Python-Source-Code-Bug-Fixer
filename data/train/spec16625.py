import numpy as np 

def function(x):

	z3 = 5
	p8 = x
	paths = []
	try:
		if x < 2:
			x = 8*x
			paths.append(1)
		else:
			z3 = 4+z3
			p8 = p8-9
			paths.append(2)
		if p8 <= 5:
			x = x/8
			x = x-2
			z3 = x-1
			paths.append(3)
		else:
			p8 = 1*x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		z3 = p8**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))