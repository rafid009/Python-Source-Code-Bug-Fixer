import numpy as np 

def function(x):

	d3 = 4
	w2 = 9
	paths = []
	try:
		if x >= 1:
			d3 = d3/w2
			paths.append(1)
		else:
			w2 = w2-5
			paths.append(2)
		if x <= 5:
			w2 = w2-w2
			d3 = d3/d3
			w2 = 3+w2
			paths.append(3)
		else:
			d3 = d3*x
			d3 = d3-7
			w2 = 3/4
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