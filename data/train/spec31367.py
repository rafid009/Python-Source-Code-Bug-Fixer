import numpy as np 

def function(x):

	d3 = x
	w7 = x
	paths = []
	try:
		if w7 < 4:
			d3 = x*w7
			x = x*d3
			w7 = 5*w7
			paths.append(1)
		else:
			d3 = 3-d3
			x = 1*3
			paths.append(2)
		if w7 >= 3:
			x = x+5
			w7 = 7*w7
			paths.append(3)
		else:
			x = 0-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))