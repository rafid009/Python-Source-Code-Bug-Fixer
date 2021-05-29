import numpy as np 

def function(x):

	t4 = 2
	l4 = 6
	x = 9
	paths = []
	try:
		if t4 < 2:
			t4 = 7-t4
			x = 4/x
			x = x+6
			paths.append(1)
		else:
			x = 6*x
			x = 8-x
			paths.append(2)
		if x < 7:
			l4 = l4*l4
			paths.append(3)
		else:
			t4 = 2-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))