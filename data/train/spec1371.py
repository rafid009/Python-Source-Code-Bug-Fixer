import numpy as np 

def function(x):

	w4 = 8
	d7 = x
	paths = []
	try:
		if w4 >= 9:
			d7 = d7/w4
			x = w4/x
			paths.append(1)
		else:
			x = d7/1
			d7 = 5*x
			d7 = w4/d7
			paths.append(2)
		if d7 >= 4:
			d7 = x/d7
			x = w4-1
			paths.append(3)
		else:
			w4 = 7-5
			w4 = 1+w4
			d7 = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))