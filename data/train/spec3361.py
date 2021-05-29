import numpy as np 

def function(x):

	z3 = 8
	z9 = 0
	paths = []
	try:
		if z9 <= 5:
			x = x+3
			z3 = 6-z3
			z9 = z9+x
			paths.append(1)
		else:
			z3 = x/z3
			paths.append(2)
		if x < 3:
			x = x-8
			x = 6/x
			paths.append(3)
		else:
			x = 6-x
			x = x*5
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))