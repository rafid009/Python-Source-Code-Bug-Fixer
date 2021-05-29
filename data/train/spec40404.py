import numpy as np 

def function(x):

	v8 = 3
	z3 = x
	paths = []
	try:
		if z3 < 8:
			z3 = z3-7
			x = 6*x
			v8 = v8+4
			paths.append(1)
		else:
			x = x/1
			z3 = v8+z3
			x = x/z3
			paths.append(2)
		if v8 <= 8:
			x = v8*x
			v8 = v8-4
			paths.append(3)
		else:
			v8 = 2+3
			z3 = 9*z3
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))