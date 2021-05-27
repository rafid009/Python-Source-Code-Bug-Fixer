import numpy as np 

def function(x):

	d3 = 5
	n2 = 8
	x = x
	paths = []
	try:
		if x >= 2:
			n2 = n2+4
			x = 0+x
			n2 = n2-x
			paths.append(1)
		else:
			x = x*8
			d3 = 7/2
			d3 = 2/x
			paths.append(2)
		if n2 < 8:
			n2 = n2-5
			x = 8-n2
			paths.append(3)
		else:
			x = d3+1
			x = x+6
			d3 = 4*d3
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		d3 = d3**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))