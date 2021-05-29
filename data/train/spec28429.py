import numpy as np 

def function(x):

	d3 = 3
	b6 = 1
	paths = []
	try:
		if b6 < 1:
			b6 = 8+x
			x = d3-4
			b6 = b6*1
			paths.append(1)
		else:
			d3 = d3/1
			paths.append(2)
		if b6 >= 3:
			d3 = d3/x
			b6 = 1/3
			paths.append(3)
		else:
			d3 = 3*d3
			b6 = x-3
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))