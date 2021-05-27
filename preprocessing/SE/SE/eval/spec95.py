import numpy as np 

def function(x):

	t0 = x
	y7 = x
	paths = []
	try:
		if x >= 3:
			y7 = y7/y7
			t0 = 3-t0
			paths.append(1)
		else:
			y7 = y7-6
			paths.append(2)
		if t0 >= 3:
			x = y7/x
			t0 = 2*t0
			t0 = 3*t0
			paths.append(3)
		else:
			t0 = t0/5
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))