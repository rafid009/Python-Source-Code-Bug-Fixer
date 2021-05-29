import numpy as np 

def function(x):

	e0 = x
	w5 = x
	paths = []
	try:
		if w5 <= 8:
			x = 9+x
			x = 6*7
			paths.append(1)
		else:
			x = x-w5
			e0 = 8+e0
			paths.append(2)
		if x >= 6:
			e0 = e0*2
			w5 = e0*6
			w5 = 6-3
			paths.append(3)
		else:
			e0 = x-9
			w5 = w5-x
			w5 = 0/w5
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		w5 = e0**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))