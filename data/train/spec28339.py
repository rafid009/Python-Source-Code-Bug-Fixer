import numpy as np 

def function(x):

	w4 = x
	j9 = x
	paths = []
	try:
		if w4 < 6:
			x = 1*x
			j9 = j9-3
			paths.append(1)
		else:
			j9 = 2+4
			j9 = 7-j9
			paths.append(2)
		if j9 < 5:
			j9 = 9+j9
			w4 = 8-w4
			paths.append(3)
		else:
			j9 = w4-j9
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