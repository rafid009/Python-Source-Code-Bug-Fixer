import numpy as np 

def function(x):

	z3 = 0
	u9 = x
	paths = []
	try:
		if x >= 6:
			x = x*z3
			x = x-x
			paths.append(1)
		else:
			z3 = 6*6
			x = x*1
			u9 = u9/1
			paths.append(2)
		if u9 > 0:
			u9 = x-u9
			x = x+u9
			paths.append(3)
		else:
			u9 = x*3
			z3 = u9*u9
			x = 2*1
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		z3 = u9**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))