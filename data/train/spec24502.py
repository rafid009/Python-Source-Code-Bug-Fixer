import numpy as np 

def function(x):

	z3 = x
	n9 = 2
	paths = []
	try:
		if n9 >= 3:
			n9 = x+6
			n9 = n9*2
			x = 4*x
			paths.append(1)
		else:
			n9 = n9*6
			x = x/7
			paths.append(2)
		if x >= 2:
			z3 = z3-1
			z3 = x+3
			paths.append(3)
		else:
			n9 = n9+n9
			x = x*1
			n9 = 5+9
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		n9 = z3**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))