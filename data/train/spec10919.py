import numpy as np 

def function(x):

	v8 = x
	z3 = 4
	paths = []
	try:
		if v8 >= 7:
			v8 = 3*2
			paths.append(1)
		else:
			v8 = v8+x
			paths.append(2)
		if v8 > 0:
			x = 4*v8
			paths.append(3)
		else:
			z3 = 5+7
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))