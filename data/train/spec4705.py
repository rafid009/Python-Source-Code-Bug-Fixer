import numpy as np 

def function(x):

	e0 = x
	w8 = x
	paths = []
	try:
		if x < 6:
			e0 = 8*5
			paths.append(1)
		else:
			w8 = w8+x
			paths.append(2)
		if w8 >= 6:
			x = 3/x
			paths.append(3)
		else:
			e0 = x*6
			w8 = x/w8
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		w8 = e0**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))