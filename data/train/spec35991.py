import numpy as np 

def function(x):

	r1 = x
	d3 = x
	paths = []
	try:
		if d3 >= 5:
			r1 = r1-5
			d3 = d3+7
			paths.append(1)
		else:
			r1 = 9+d3
			paths.append(2)
		if r1 > 5:
			r1 = 4*r1
			paths.append(3)
		else:
			r1 = r1+8
			r1 = d3-r1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d3 = x**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))