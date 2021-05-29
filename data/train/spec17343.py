import numpy as np 

def function(x):

	t3 = 9
	u0 = x
	paths = []
	try:
		if t3 <= 9:
			t3 = t3*7
			paths.append(1)
		else:
			t3 = 6*x
			paths.append(2)
		if t3 < 6:
			u0 = 6*u0
			u0 = t3*u0
			paths.append(3)
		else:
			t3 = t3*x
			u0 = 8/u0
			u0 = t3-u0
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