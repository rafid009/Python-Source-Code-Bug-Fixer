import numpy as np 

def function(x):

	d3 = 7
	w3 = x
	paths = []
	try:
		if x > 9:
			d3 = 5+x
			paths.append(1)
		else:
			w3 = 0-d3
			w3 = x/7
			d3 = d3*9
			paths.append(2)
		if d3 > 8:
			d3 = 9-6
			paths.append(3)
		else:
			x = d3+x
			w3 = x-1
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		d3 = w3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))