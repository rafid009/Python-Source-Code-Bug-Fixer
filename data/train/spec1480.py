import numpy as np 

def function(x):

	w8 = x
	x0 = 1
	paths = []
	try:
		if w8 > 5:
			x0 = 8/x0
			paths.append(1)
		else:
			x0 = x0*6
			x0 = 1*x
			x = x/2
			paths.append(2)
		if x0 < 1:
			w8 = w8-5
			paths.append(3)
		else:
			w8 = w8-0
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x0 = w8**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))