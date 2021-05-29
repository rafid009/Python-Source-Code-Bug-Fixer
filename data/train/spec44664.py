import numpy as np 

def function(x):

	w4 = x
	x0 = 8
	paths = []
	try:
		if x0 <= 7:
			w4 = x0+w4
			w4 = 8*w4
			paths.append(1)
		else:
			x0 = 6*6
			x = 6*x
			x = x/x
			paths.append(2)
		if x <= 6:
			x = 6*x
			x = x/4
			x0 = x0/9
			paths.append(3)
		else:
			x0 = 4/3
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))