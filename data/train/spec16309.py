import numpy as np 

def function(x):

	d3 = 1
	b9 = x
	paths = []
	try:
		if d3 >= 9:
			x = x+3
			paths.append(1)
		else:
			d3 = 6+d3
			d3 = 7-d3
			paths.append(2)
		if x < 2:
			x = 9/x
			d3 = 7*d3
			paths.append(3)
		else:
			d3 = 5*1
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))