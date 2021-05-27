import numpy as np 

def function(x):

	z3 = 3
	w7 = x
	paths = []
	try:
		if w7 <= 5:
			z3 = z3-8
			paths.append(1)
		else:
			z3 = x*z3
			z3 = z3*2
			z3 = 2+3
			paths.append(2)
		if z3 <= 7:
			x = x*2
			x = x+6
			paths.append(3)
		else:
			x = w7/z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		w7 = z3**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))