import numpy as np 

def function(x):

	z0 = x
	t0 = x
	paths = []
	try:
		if t0 > 4:
			x = 5*x
			paths.append(1)
		else:
			t0 = 5-t0
			paths.append(2)
		if z0 < 2:
			x = 9*2
			x = z0-x
			paths.append(3)
		else:
			x = x+0
			t0 = x-6
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