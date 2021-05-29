import numpy as np 

def function(x):

	z3 = 2
	t4 = 1
	paths = []
	try:
		if x >= 1:
			t4 = t4*9
			z3 = 7+z3
			paths.append(1)
		else:
			x = x+7
			z3 = z3/8
			paths.append(2)
		if x >= 3:
			t4 = t4*t4
			t4 = 4/t4
			paths.append(3)
		else:
			x = 5/x
			t4 = t4+x
			t4 = t4-z3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))