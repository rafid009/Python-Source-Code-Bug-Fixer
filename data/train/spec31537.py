import numpy as np 

def function(x):

	t0 = 6
	w8 = 5
	paths = []
	try:
		if x > 4:
			t0 = 0-9
			paths.append(1)
		else:
			x = 1*x
			t0 = 1/w8
			paths.append(2)
		if x <= 9:
			t0 = t0-t0
			paths.append(3)
		else:
			w8 = w8+t0
			x = x-x
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