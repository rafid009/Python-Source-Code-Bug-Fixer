import numpy as np 

def function(x):

	w8 = 6
	d8 = x
	paths = []
	try:
		if w8 < 6:
			x = x/8
			paths.append(1)
		else:
			d8 = 4-d8
			w8 = w8-3
			d8 = 3*d8
			paths.append(2)
		if d8 <= 8:
			x = 4+w8
			w8 = w8*1
			paths.append(3)
		else:
			d8 = d8+5
			x = x+x
			d8 = d8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))