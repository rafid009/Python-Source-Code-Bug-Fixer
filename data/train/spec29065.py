import numpy as np 

def function(x):

	t0 = 5
	f0 = 3
	x = 9
	paths = []
	try:
		if x > 6:
			x = t0-x
			f0 = 9/f0
			paths.append(1)
		else:
			x = 8-6
			f0 = f0/6
			paths.append(2)
		if t0 < 6:
			f0 = f0-6
			f0 = f0-x
			f0 = f0*t0
			paths.append(3)
		else:
			f0 = f0-4
			t0 = 3-t0
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