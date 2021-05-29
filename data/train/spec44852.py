import numpy as np 

def function(x):

	t0 = 6
	v5 = 5
	paths = []
	try:
		if x >= 7:
			t0 = 6*t0
			paths.append(1)
		else:
			v5 = 1-v5
			paths.append(2)
		if v5 < 3:
			v5 = v5*6
			t0 = t0/5
			paths.append(3)
		else:
			v5 = v5-4
			v5 = 8/v5
			t0 = 4-x
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