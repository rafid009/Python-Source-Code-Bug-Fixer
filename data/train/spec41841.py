import numpy as np 

def function(x):

	b5 = x
	d3 = x
	paths = []
	try:
		if x >= 2:
			d3 = 1*d3
			d3 = 5/d3
			d3 = x/b5
			paths.append(1)
		else:
			d3 = d3*b5
			paths.append(2)
		if d3 > 5:
			b5 = 7+0
			x = 4+x
			paths.append(3)
		else:
			x = d3-d3
			b5 = 5/b5
			b5 = 0/b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))