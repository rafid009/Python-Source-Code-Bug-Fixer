import numpy as np 

def function(x):

	w2 = x
	d8 = x
	paths = []
	try:
		if d8 <= 9:
			x = 8/x
			d8 = d8*2
			w2 = w2-5
			paths.append(1)
		else:
			x = x/x
			x = x/9
			paths.append(2)
		if w2 <= 0:
			w2 = w2/w2
			d8 = 6-w2
			w2 = 1-8
			paths.append(3)
		else:
			w2 = 9*w2
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