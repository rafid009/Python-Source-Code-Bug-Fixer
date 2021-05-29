import numpy as np 

def function(x):

	d3 = 1
	p3 = 3
	paths = []
	try:
		if p3 >= 5:
			d3 = 0-6
			d3 = 2/d3
			d3 = d3/1
			paths.append(1)
		else:
			x = x-7
			p3 = 0/p3
			p3 = p3/3
			paths.append(2)
		if p3 > 0:
			x = 0-x
			d3 = d3-2
			paths.append(3)
		else:
			p3 = 4-p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))