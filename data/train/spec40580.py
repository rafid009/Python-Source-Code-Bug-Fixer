import numpy as np 

def function(x):

	t0 = x
	w4 = 2
	paths = []
	try:
		if x < 8:
			w4 = w4*7
			x = 3/w4
			w4 = w4-x
			paths.append(1)
		else:
			x = 7*w4
			paths.append(2)
		if t0 >= 7:
			x = 4+x
			t0 = t0-9
			paths.append(3)
		else:
			x = 4/x
			x = 9+x
			x = x/x
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