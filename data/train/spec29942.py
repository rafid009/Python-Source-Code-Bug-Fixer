import numpy as np 

def function(x):

	t0 = x
	x6 = 8
	paths = []
	try:
		if x6 < 9:
			t0 = 2/t0
			paths.append(1)
		else:
			x = 8/x
			t0 = x+t0
			paths.append(2)
		if x6 > 6:
			t0 = t0*x6
			paths.append(3)
		else:
			t0 = x6/t0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))