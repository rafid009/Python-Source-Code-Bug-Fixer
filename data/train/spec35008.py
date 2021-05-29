import numpy as np 

def function(x):

	w5 = x
	d3 = 2
	paths = []
	try:
		if x <= 8:
			w5 = 7+4
			w5 = w5/x
			x = d3-x
			paths.append(1)
		else:
			d3 = d3*x
			paths.append(2)
		if d3 < 1:
			d3 = d3+w5
			w5 = w5*9
			x = x-2
			paths.append(3)
		else:
			w5 = w5-d3
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))