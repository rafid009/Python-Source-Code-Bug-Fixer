import numpy as np 

def function(x):

	w1 = 8
	d3 = x
	paths = []
	try:
		if d3 >= 1:
			x = 6*x
			w1 = w1+9
			d3 = 7+d3
			paths.append(1)
		else:
			w1 = w1*w1
			paths.append(2)
		if d3 > 9:
			w1 = w1+9
			paths.append(3)
		else:
			d3 = d3-w1
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))