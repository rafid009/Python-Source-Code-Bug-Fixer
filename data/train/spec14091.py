import numpy as np 

def function(x):

	d3 = 8
	o4 = x
	paths = []
	try:
		if o4 > 1:
			x = 7*0
			x = o4+7
			o4 = o4*9
			paths.append(1)
		else:
			d3 = 5*d3
			paths.append(2)
		if x >= 3:
			o4 = o4-6
			o4 = 6+o4
			paths.append(3)
		else:
			d3 = x-1
			x = 8-d3
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		o4 = d3**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))