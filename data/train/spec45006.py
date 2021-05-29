import numpy as np 

def function(x):

	l3 = x
	d3 = x
	paths = []
	try:
		if d3 > 3:
			d3 = d3*l3
			paths.append(1)
		else:
			x = l3+9
			l3 = x/3
			paths.append(2)
		if x >= 3:
			l3 = d3+2
			l3 = 7/x
			l3 = l3+8
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert d3 >= 0
		x = d3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))