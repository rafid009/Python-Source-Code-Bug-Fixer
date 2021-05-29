import numpy as np 

def function(x):

	q2 = x
	z3 = x
	paths = []
	try:
		if z3 < 3:
			z3 = 9/9
			z3 = 9-z3
			paths.append(1)
		else:
			q2 = q2-0
			q2 = 1+z3
			paths.append(2)
		if z3 > 6:
			z3 = z3*0
			z3 = 1+z3
			z3 = z3/8
			paths.append(3)
		else:
			q2 = q2+8
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))