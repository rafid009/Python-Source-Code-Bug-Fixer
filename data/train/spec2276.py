import numpy as np 

def function(x):

	w5 = 1
	w4 = x
	paths = []
	try:
		if w4 > 2:
			x = 7*w4
			paths.append(1)
		else:
			w5 = 1+8
			w4 = w4-9
			paths.append(2)
		if x >= 2:
			w4 = 2+w4
			w5 = 4*w5
			paths.append(3)
		else:
			x = x*3
			w5 = 0-w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w4 = w5**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))