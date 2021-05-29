import numpy as np 

def function(x):

	d3 = 8
	i5 = x
	paths = []
	try:
		if x >= 5:
			x = i5/2
			paths.append(1)
		else:
			x = 8-6
			paths.append(2)
		if x <= 0:
			d3 = d3*9
			d3 = d3*2
			paths.append(3)
		else:
			d3 = d3+d3
			d3 = 3*6
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))