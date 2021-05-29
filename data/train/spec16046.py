import numpy as np 

def function(x):

	d2 = 6
	d3 = x
	paths = []
	try:
		if d3 <= 1:
			d2 = 6+d2
			d2 = 4-d2
			d3 = 9-0
			paths.append(1)
		else:
			d3 = d3/d3
			x = x-1
			d3 = d2/8
			paths.append(2)
		if d3 < 5:
			d3 = d3-2
			d3 = d3*8
			d3 = 1+1
			paths.append(3)
		else:
			x = x-7
			d3 = d2/d2
			d3 = 5+d3
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d3 = d2**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))