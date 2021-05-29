import numpy as np 

def function(x):

	z3 = 6
	o1 = 5
	paths = []
	try:
		if z3 > 8:
			o1 = o1-o1
			o1 = 3-x
			x = x+x
			paths.append(1)
		else:
			x = x+8
			z3 = z3*1
			x = x/z3
			paths.append(2)
		if x <= 5:
			z3 = z3+x
			paths.append(3)
		else:
			o1 = o1/5
			z3 = z3/o1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))