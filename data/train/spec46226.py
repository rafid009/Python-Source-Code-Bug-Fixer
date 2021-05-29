import numpy as np 

def function(x):

	z3 = x
	v6 = x
	paths = []
	try:
		if v6 <= 2:
			v6 = v6*4
			v6 = v6+4
			paths.append(1)
		else:
			x = 8/x
			x = 0-x
			x = x*1
			paths.append(2)
		if v6 <= 0:
			z3 = z3+8
			v6 = v6*5
			v6 = 5-v6
			paths.append(3)
		else:
			z3 = 5*z3
			x = 5+1
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))