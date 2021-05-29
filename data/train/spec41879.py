import numpy as np 

def function(x):

	z3 = 2
	v6 = 7
	paths = []
	try:
		if x <= 2:
			v6 = 7*9
			z3 = 8*z3
			x = 9*x
			paths.append(1)
		else:
			z3 = v6/v6
			x = x+x
			v6 = 1*v6
			paths.append(2)
		if z3 < 6:
			x = x/7
			z3 = v6+z3
			v6 = x/v6
			paths.append(3)
		else:
			v6 = x+0
			x = 8+v6
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))