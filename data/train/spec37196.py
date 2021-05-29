import numpy as np 

def function(x):

	w4 = 1
	z3 = 7
	paths = []
	try:
		if x < 1:
			w4 = z3*z3
			z3 = z3/x
			paths.append(1)
		else:
			w4 = w4*0
			w4 = 8-w4
			paths.append(2)
		if z3 >= 7:
			x = x-6
			w4 = x-7
			x = x*4
			paths.append(3)
		else:
			w4 = x+2
			x = 8-x
			w4 = 3+w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))