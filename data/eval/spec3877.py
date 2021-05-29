import numpy as np 

def function(x):

	z3 = x
	i8 = 9
	paths = []
	try:
		if x < 8:
			x = x*2
			z3 = 4-3
			i8 = 2*i8
			paths.append(1)
		else:
			i8 = i8*3
			z3 = 1+z3
			paths.append(2)
		if x <= 9:
			i8 = z3+0
			z3 = z3*i8
			z3 = 0-x
			paths.append(3)
		else:
			i8 = i8/x
			x = 2-z3
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		i8 = z3**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))