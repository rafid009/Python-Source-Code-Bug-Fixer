import numpy as np 

def function(x):

	b7 = 3
	d3 = 4
	paths = []
	try:
		if b7 < 8:
			d3 = 2*0
			x = 5/x
			paths.append(1)
		else:
			b7 = b7/9
			paths.append(2)
		if x >= 8:
			x = x-7
			paths.append(3)
		else:
			d3 = x/b7
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