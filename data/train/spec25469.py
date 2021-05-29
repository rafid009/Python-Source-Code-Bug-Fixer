import numpy as np 

def function(x):

	r8 = x
	z3 = 2
	x = 2
	paths = []
	try:
		if z3 > 0:
			z3 = z3*z3
			r8 = r8/7
			paths.append(1)
		else:
			r8 = 8+r8
			r8 = r8*x
			r8 = r8+x
			paths.append(2)
		if r8 < 2:
			x = 2*x
			paths.append(3)
		else:
			z3 = 8/z3
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		z3 = r8**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))