import numpy as np 

def function(x):

	l7 = 8
	z3 = x
	x = 0
	paths = []
	try:
		if x <= 9:
			l7 = 5*6
			x = 4-1
			paths.append(1)
		else:
			z3 = 4+z3
			l7 = 7*l7
			paths.append(2)
		if x > 8:
			x = x*4
			z3 = 9*0
			paths.append(3)
		else:
			x = 2+x
			l7 = 1-l7
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