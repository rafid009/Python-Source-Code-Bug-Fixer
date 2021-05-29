import numpy as np 

def function(x):

	z3 = 4
	p1 = 5
	paths = []
	try:
		if x > 7:
			p1 = 3*p1
			p1 = z3*7
			z3 = z3/3
			paths.append(1)
		else:
			p1 = 4-p1
			z3 = 4/z3
			z3 = x*p1
			paths.append(2)
		if z3 > 8:
			x = x+4
			p1 = 4/p1
			paths.append(3)
		else:
			p1 = 2*5
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))