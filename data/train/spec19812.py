import numpy as np 

def function(x):

	z3 = x
	r1 = 4
	x = x
	paths = []
	try:
		if x <= 2:
			z3 = z3*0
			z3 = z3+7
			paths.append(1)
		else:
			r1 = r1*4
			paths.append(2)
		if z3 >= 9:
			z3 = z3*5
			z3 = z3/z3
			paths.append(3)
		else:
			r1 = r1+9
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