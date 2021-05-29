import numpy as np 

def function(x):

	t1 = 6
	z3 = x
	paths = []
	try:
		if t1 > 6:
			z3 = 9*1
			paths.append(1)
		else:
			t1 = t1+5
			x = 2-z3
			paths.append(2)
		if x <= 6:
			t1 = 0*t1
			x = x/5
			x = 0/x
			paths.append(3)
		else:
			z3 = z3+9
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