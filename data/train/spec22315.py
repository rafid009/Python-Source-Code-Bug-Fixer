import numpy as np 

def function(x):

	i1 = x
	t0 = x
	paths = []
	try:
		if x > 3:
			x = 9*x
			paths.append(1)
		else:
			t0 = 2*t0
			paths.append(2)
		if x <= 5:
			t0 = 5+t0
			paths.append(3)
		else:
			i1 = i1+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))