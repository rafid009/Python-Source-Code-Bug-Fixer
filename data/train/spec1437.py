import numpy as np 

def function(x):

	d3 = 5
	n8 = x
	paths = []
	try:
		if n8 <= 0:
			x = 6/x
			d3 = d3+n8
			paths.append(1)
		else:
			x = 6+7
			paths.append(2)
		if n8 > 9:
			n8 = n8/9
			n8 = n8-9
			paths.append(3)
		else:
			d3 = 2*1
			x = n8/6
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