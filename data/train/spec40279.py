import numpy as np 

def function(x):

	z3 = x
	p2 = x
	paths = []
	try:
		if x < 4:
			z3 = z3/1
			x = 9-x
			paths.append(1)
		else:
			z3 = z3/4
			x = x/z3
			paths.append(2)
		if z3 <= 3:
			x = p2*0
			paths.append(3)
		else:
			z3 = x-1
			z3 = z3*2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))