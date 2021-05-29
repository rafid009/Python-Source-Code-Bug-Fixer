import numpy as np 

def function(x):

	d3 = 6
	l3 = x
	paths = []
	try:
		if x >= 8:
			d3 = l3-d3
			paths.append(1)
		else:
			d3 = 1*d3
			x = x*9
			d3 = d3-2
			paths.append(2)
		if l3 > 6:
			d3 = d3/9
			x = x*4
			l3 = 3+3
			paths.append(3)
		else:
			l3 = l3-4
			x = x*x
			d3 = x-3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		d3 = l3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))