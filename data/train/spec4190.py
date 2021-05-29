import numpy as np 

def function(x):

	d5 = x
	w7 = 2
	paths = []
	try:
		if x < 6:
			w7 = d5+8
			d5 = d5/4
			paths.append(1)
		else:
			d5 = w7/7
			paths.append(2)
		if w7 >= 8:
			x = x-d5
			x = x-9
			d5 = x-d5
			paths.append(3)
		else:
			d5 = d5*w7
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))