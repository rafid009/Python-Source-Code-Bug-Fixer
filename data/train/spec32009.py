import numpy as np 

def function(x):

	d1 = 3
	w2 = x
	x = 6
	paths = []
	try:
		if w2 > 0:
			w2 = w2+4
			d1 = 9/x
			paths.append(1)
		else:
			w2 = w2+4
			d1 = 1/d1
			x = 9*6
			paths.append(2)
		if x >= 0:
			x = x+x
			x = 6/x
			x = w2*3
			paths.append(3)
		else:
			d1 = d1+0
			w2 = w2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))