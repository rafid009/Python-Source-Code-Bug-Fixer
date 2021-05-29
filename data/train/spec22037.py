import numpy as np 

def function(x):

	z3 = x
	v3 = 9
	paths = []
	try:
		if z3 <= 9:
			x = v3-x
			v3 = 5*2
			x = v3*4
			paths.append(1)
		else:
			x = x/8
			z3 = v3-6
			x = v3+8
			paths.append(2)
		if z3 >= 5:
			z3 = 4*6
			v3 = 6+8
			v3 = v3*v3
			paths.append(3)
		else:
			v3 = 3-z3
			v3 = 0-v3
			v3 = 2*v3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		v3 = z3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))