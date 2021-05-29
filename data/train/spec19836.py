import numpy as np 

def function(x):

	t0 = x
	o0 = 3
	paths = []
	try:
		if t0 > 0:
			t0 = 8-t0
			paths.append(1)
		else:
			t0 = t0*x
			t0 = 8-4
			paths.append(2)
		if x > 3:
			t0 = t0-6
			paths.append(3)
		else:
			t0 = 9+t0
			t0 = 7+o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))