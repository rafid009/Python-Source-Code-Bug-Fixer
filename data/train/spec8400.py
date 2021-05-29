import numpy as np 

def function(x):

	z3 = x
	p2 = x
	x = 0
	paths = []
	try:
		if p2 <= 2:
			p2 = 2+p2
			z3 = 3+z3
			paths.append(1)
		else:
			p2 = p2-8
			paths.append(2)
		if z3 > 9:
			x = x*7
			x = 6-z3
			x = 9/x
			paths.append(3)
		else:
			z3 = z3+9
			p2 = 3+p2
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