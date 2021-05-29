import numpy as np 

def function(x):

	l3 = x
	d3 = 4
	paths = []
	try:
		if x >= 3:
			d3 = 1/5
			paths.append(1)
		else:
			l3 = 7+7
			l3 = l3-6
			d3 = d3/8
			paths.append(2)
		if l3 > 7:
			l3 = 9-l3
			paths.append(3)
		else:
			l3 = l3*x
			d3 = l3+7
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