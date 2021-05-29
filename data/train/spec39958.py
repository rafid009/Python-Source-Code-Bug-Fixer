import numpy as np 

def function(x):

	w4 = 1
	f4 = 1
	paths = []
	try:
		if x <= 7:
			f4 = 0+w4
			w4 = w4*f4
			f4 = f4*w4
			paths.append(1)
		else:
			x = w4/4
			paths.append(2)
		if x > 6:
			f4 = f4-8
			w4 = x*w4
			x = x+3
			paths.append(3)
		else:
			w4 = 9*x
			x = w4-x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		w4 = f4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))