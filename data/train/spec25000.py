import numpy as np 

def function(x):

	w6 = x
	z3 = 6
	paths = []
	try:
		if z3 >= 1:
			x = x/5
			z3 = w6/x
			w6 = 6-w6
			paths.append(1)
		else:
			x = x*5
			z3 = z3*8
			paths.append(2)
		if z3 < 4:
			z3 = x/7
			z3 = z3-0
			w6 = 4*w6
			paths.append(3)
		else:
			x = x*z3
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))