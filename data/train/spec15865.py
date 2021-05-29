import numpy as np 

def function(x):

	d7 = 5
	w9 = 4
	paths = []
	try:
		if d7 >= 9:
			d7 = d7*5
			x = x+x
			paths.append(1)
		else:
			d7 = d7-x
			w9 = d7*2
			x = x-w9
			paths.append(2)
		if w9 > 8:
			w9 = w9/x
			x = 1-x
			d7 = x-6
			paths.append(3)
		else:
			x = x-w9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))