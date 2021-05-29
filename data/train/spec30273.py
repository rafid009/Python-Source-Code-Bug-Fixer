import numpy as np 

def function(x):

	d4 = 0
	w4 = x
	x = x
	paths = []
	try:
		if w4 >= 7:
			w4 = 6+w4
			paths.append(1)
		else:
			d4 = d4-8
			w4 = 4/x
			x = x-7
			paths.append(2)
		if x >= 6:
			d4 = d4-9
			x = x*6
			paths.append(3)
		else:
			x = x+3
			d4 = 1+5
			d4 = w4-9
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		w4 = d4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))