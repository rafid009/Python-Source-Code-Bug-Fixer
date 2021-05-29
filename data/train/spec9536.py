import numpy as np 

def function(x):

	z3 = x
	v0 = x
	paths = []
	try:
		if v0 < 1:
			x = z3/8
			x = 5*7
			x = 2/1
			paths.append(1)
		else:
			v0 = v0-5
			z3 = 2+z3
			paths.append(2)
		if v0 < 2:
			v0 = v0-2
			v0 = 2*v0
			x = 3/8
			paths.append(3)
		else:
			v0 = z3-9
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))