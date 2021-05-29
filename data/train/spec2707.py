import numpy as np 

def function(x):

	z3 = 2
	s5 = 2
	paths = []
	try:
		if s5 > 4:
			z3 = z3*2
			s5 = s5+8
			paths.append(1)
		else:
			z3 = z3-3
			paths.append(2)
		if x < 4:
			s5 = s5/s5
			paths.append(3)
		else:
			z3 = z3*0
			z3 = z3+3
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