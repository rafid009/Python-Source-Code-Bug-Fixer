import numpy as np 

def function(x):

	z3 = 5
	j3 = 3
	paths = []
	try:
		if z3 < 2:
			j3 = j3-4
			z3 = j3/6
			x = x/8
			paths.append(1)
		else:
			z3 = z3*z3
			paths.append(2)
		if j3 <= 1:
			x = j3*x
			x = x*4
			x = 5-z3
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))