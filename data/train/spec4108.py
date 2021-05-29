import numpy as np 

def function(x):

	j8 = 0
	z3 = 3
	paths = []
	try:
		if j8 <= 1:
			x = 1+x
			z3 = z3+5
			paths.append(1)
		else:
			z3 = z3+6
			x = z3+1
			x = x*x
			paths.append(2)
		if x <= 0:
			j8 = 4-6
			paths.append(3)
		else:
			j8 = 7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))