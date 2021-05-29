import numpy as np 

def function(x):

	i3 = x
	z3 = x
	x = 2
	paths = []
	try:
		if i3 <= 9:
			x = x/4
			paths.append(1)
		else:
			x = x-i3
			paths.append(2)
		if x >= 1:
			x = 0-x
			i3 = i3+2
			i3 = i3-6
			paths.append(3)
		else:
			i3 = 9*x
			x = i3-z3
			z3 = z3-x
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		z3 = i3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))