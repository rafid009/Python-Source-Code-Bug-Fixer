import numpy as np 

def function(x):

	e5 = x
	t0 = x
	x = x
	paths = []
	try:
		if x <= 9:
			e5 = 8+e5
			paths.append(1)
		else:
			t0 = 4+1
			t0 = 0+t0
			t0 = t0-x
			paths.append(2)
		if x <= 0:
			t0 = t0/4
			t0 = 5/x
			paths.append(3)
		else:
			x = t0*x
			x = x-t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))