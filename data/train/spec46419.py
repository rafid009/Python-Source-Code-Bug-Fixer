import numpy as np 

def function(x):

	z3 = 6
	t6 = 5
	paths = []
	try:
		if t6 > 1:
			t6 = t6*t6
			paths.append(1)
		else:
			t6 = 7-6
			x = x/4
			paths.append(2)
		if x >= 2:
			z3 = 4+0
			z3 = z3*6
			paths.append(3)
		else:
			t6 = 4-t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))