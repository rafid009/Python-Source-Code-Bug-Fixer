import numpy as np 

def function(x):

	v7 = x
	z3 = 5
	paths = []
	try:
		if z3 < 7:
			z3 = 8*6
			x = x*1
			v7 = x+x
			paths.append(1)
		else:
			z3 = 1+v7
			z3 = 6/9
			v7 = 3/3
			paths.append(2)
		if x >= 3:
			z3 = z3-3
			v7 = 6-v7
			v7 = 1*3
			paths.append(3)
		else:
			v7 = v7-v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))