import numpy as np 

def function(x):

	d8 = 2
	n8 = x
	paths = []
	try:
		if n8 >= 1:
			d8 = d8-d8
			paths.append(1)
		else:
			d8 = 7-d8
			d8 = 4-d8
			x = x*6
			paths.append(2)
		if d8 <= 1:
			d8 = d8+d8
			d8 = 3-d8
			paths.append(3)
		else:
			d8 = d8/7
			d8 = d8/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))