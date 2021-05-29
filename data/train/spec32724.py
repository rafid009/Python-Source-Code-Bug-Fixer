import numpy as np 

def function(x):

	o2 = x
	z3 = x
	paths = []
	try:
		if z3 >= 4:
			z3 = 2-z3
			paths.append(1)
		else:
			x = o2+z3
			o2 = o2*8
			o2 = 1*o2
			paths.append(2)
		if x >= 4:
			z3 = z3+1
			paths.append(3)
		else:
			z3 = z3/5
			x = 5-o2
			o2 = o2*o2
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))