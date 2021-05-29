import numpy as np 

def function(x):

	a2 = 0
	z3 = 5
	paths = []
	try:
		if a2 > 2:
			x = 9+x
			z3 = z3/a2
			paths.append(1)
		else:
			a2 = 7+z3
			z3 = 0-a2
			x = 3/x
			paths.append(2)
		if z3 < 0:
			x = x+5
			x = 7*1
			a2 = a2*z3
			paths.append(3)
		else:
			z3 = a2+0
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		a2 = z3**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))