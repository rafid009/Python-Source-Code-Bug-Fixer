import numpy as np 

def function(x):

	z3 = x
	f0 = x
	x = x
	paths = []
	try:
		if x > 8:
			x = z3*x
			paths.append(1)
		else:
			z3 = 8*z3
			paths.append(2)
		if x <= 8:
			f0 = x*6
			f0 = 1+f0
			paths.append(3)
		else:
			z3 = z3+x
			z3 = 1+z3
			f0 = f0/1
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))