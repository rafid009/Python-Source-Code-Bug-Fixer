import numpy as np 

def function(x):

	t4 = 0
	w4 = 1
	x = x
	paths = []
	try:
		if x <= 0:
			w4 = t4+6
			paths.append(1)
		else:
			x = x-5
			x = x-x
			x = x/w4
			paths.append(2)
		if x <= 3:
			x = x*5
			x = x-1
			t4 = 3*w4
			paths.append(3)
		else:
			w4 = x/w4
			x = 5-x
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))