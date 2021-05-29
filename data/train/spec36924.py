import numpy as np 

def function(x):

	v3 = 8
	t0 = 8
	x = x
	paths = []
	try:
		if x <= 6:
			t0 = 9*t0
			paths.append(1)
		else:
			v3 = v3+2
			v3 = x-8
			paths.append(2)
		if v3 <= 7:
			v3 = v3/8
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))