import numpy as np 

def function(x):

	z3 = x
	s5 = x
	paths = []
	try:
		if x <= 5:
			z3 = 7*2
			z3 = z3-8
			z3 = z3-9
			paths.append(1)
		else:
			x = 3+x
			s5 = s5*4
			z3 = 8*z3
			paths.append(2)
		if z3 >= 8:
			z3 = 2*s5
			z3 = 0/7
			paths.append(3)
		else:
			z3 = 6*x
			s5 = s5/5
			x = x-7
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))