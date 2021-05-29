import numpy as np 

def function(x):

	k6 = 6
	d3 = 0
	paths = []
	try:
		if k6 < 3:
			k6 = k6/4
			paths.append(1)
		else:
			k6 = d3/k6
			paths.append(2)
		if d3 >= 0:
			d3 = d3/1
			paths.append(3)
		else:
			k6 = k6*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))