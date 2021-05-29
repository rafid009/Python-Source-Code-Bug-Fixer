import numpy as np 

def function(x):

	d3 = 7
	j4 = 3
	paths = []
	try:
		if x >= 1:
			j4 = 7+1
			d3 = d3/6
			j4 = 2-j4
			paths.append(1)
		else:
			d3 = d3-d3
			paths.append(2)
		if x > 5:
			d3 = d3-5
			paths.append(3)
		else:
			x = x/4
			x = x+j4
			j4 = 4*9
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