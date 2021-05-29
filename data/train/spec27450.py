import numpy as np 

def function(x):

	z3 = 5
	t4 = x
	paths = []
	try:
		if x < 6:
			x = 0*x
			paths.append(1)
		else:
			x = x*2
			x = 5+x
			paths.append(2)
		if t4 >= 7:
			x = x/5
			t4 = 2-t4
			paths.append(3)
		else:
			t4 = z3-5
			t4 = t4+7
			z3 = 5/z3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		z3 = t4**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))