import numpy as np 

def function(x):

	e0 = x
	w8 = 9
	paths = []
	try:
		if w8 <= 0:
			w8 = w8+w8
			e0 = 8*5
			x = x+e0
			paths.append(1)
		else:
			e0 = e0/w8
			paths.append(2)
		if w8 > 8:
			x = x+8
			e0 = 7-e0
			w8 = 2*2
			paths.append(3)
		else:
			w8 = x/w8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))