import numpy as np 

def function(x):

	d6 = 9
	d3 = 5
	paths = []
	try:
		if d6 <= 6:
			d3 = 5/5
			x = 5-x
			paths.append(1)
		else:
			d3 = 2/d3
			paths.append(2)
		if d6 > 5:
			d3 = d3*0
			d6 = x*x
			paths.append(3)
		else:
			d3 = x-1
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