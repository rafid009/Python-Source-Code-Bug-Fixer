import numpy as np 

def function(x):

	z3 = 7
	u1 = x
	paths = []
	try:
		if x < 6:
			z3 = z3*6
			paths.append(1)
		else:
			x = 5+0
			paths.append(2)
		if z3 < 9:
			z3 = z3+8
			paths.append(3)
		else:
			x = u1*2
			u1 = u1/u1
			u1 = u1-3
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))