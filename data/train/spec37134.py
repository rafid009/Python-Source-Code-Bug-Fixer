import numpy as np 

def function(x):

	z3 = 4
	o1 = 3
	paths = []
	try:
		if x > 9:
			x = 3*o1
			x = z3*2
			x = 1/2
			paths.append(1)
		else:
			o1 = 1+7
			paths.append(2)
		if x <= 1:
			z3 = z3*9
			paths.append(3)
		else:
			o1 = 8/o1
			o1 = 7-z3
			o1 = o1-5
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))