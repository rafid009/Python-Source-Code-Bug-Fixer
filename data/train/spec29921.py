import numpy as np 

def function(x):

	k6 = x
	w8 = x
	paths = []
	try:
		if w8 < 7:
			w8 = w8/5
			k6 = k6-3
			w8 = k6/x
			paths.append(1)
		else:
			x = w8-8
			k6 = k6+5
			paths.append(2)
		if w8 < 6:
			k6 = 7/1
			w8 = w8+2
			paths.append(3)
		else:
			k6 = k6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))