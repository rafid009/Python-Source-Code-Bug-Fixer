import numpy as np 

def function(x):

	w4 = 4
	w8 = x
	paths = []
	try:
		if x < 7:
			x = w8+w4
			x = w4-x
			w8 = x-w8
			paths.append(1)
		else:
			x = x*8
			w8 = 4-w4
			paths.append(2)
		if x < 3:
			w4 = 6-w8
			x = 2-1
			paths.append(3)
		else:
			w8 = 6+w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))