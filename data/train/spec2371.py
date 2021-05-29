import numpy as np 

def function(x):

	d3 = 8
	e8 = x
	paths = []
	try:
		if e8 < 6:
			e8 = e8-d3
			d3 = 6*d3
			e8 = e8-4
			paths.append(1)
		else:
			d3 = d3/d3
			paths.append(2)
		if d3 <= 7:
			d3 = e8+5
			e8 = 0*e8
			paths.append(3)
		else:
			e8 = e8-6
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))