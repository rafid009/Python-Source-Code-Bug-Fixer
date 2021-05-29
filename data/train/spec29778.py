import numpy as np 

def function(x):

	q6 = 5
	d3 = 1
	paths = []
	try:
		if d3 < 3:
			q6 = 8-q6
			x = x/d3
			q6 = 2/d3
			paths.append(1)
		else:
			d3 = d3*8
			d3 = d3-d3
			d3 = 8*d3
			paths.append(2)
		if x > 8:
			q6 = q6-0
			paths.append(3)
		else:
			d3 = d3/x
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		q6 = d3**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))