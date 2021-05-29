import numpy as np 

def function(x):

	z3 = 4
	k7 = x
	x = 0
	paths = []
	try:
		if k7 <= 1:
			x = x*k7
			k7 = k7*8
			z3 = 2/k7
			paths.append(1)
		else:
			k7 = 1-k7
			paths.append(2)
		if k7 <= 8:
			x = 5+x
			k7 = z3*k7
			k7 = 2/k7
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))