import numpy as np 

def function(x):

	a4 = 2
	w8 = x
	paths = []
	try:
		if x >= 3:
			w8 = 8+w8
			a4 = 4*a4
			w8 = 6-w8
			paths.append(1)
		else:
			w8 = w8+5
			a4 = 5*4
			paths.append(2)
		if x > 7:
			w8 = w8+w8
			paths.append(3)
		else:
			a4 = 7/w8
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		w8 = a4**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))