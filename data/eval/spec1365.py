import numpy as np 

def function(x):

	d3 = x
	q7 = 6
	x = 7
	paths = []
	try:
		if d3 < 4:
			d3 = d3+d3
			paths.append(1)
		else:
			q7 = 1-q7
			paths.append(2)
		if d3 >= 9:
			q7 = 1/q7
			q7 = q7*8
			q7 = 4-q7
			paths.append(3)
		else:
			x = q7+x
			x = x/d3
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		d3 = q7**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))