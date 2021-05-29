import numpy as np 

def function(x):

	d3 = x
	p5 = 1
	paths = []
	try:
		if x >= 0:
			x = x/7
			d3 = d3/3
			paths.append(1)
		else:
			d3 = 6+d3
			d3 = x+2
			paths.append(2)
		if x > 8:
			x = x*4
			d3 = d3+7
			paths.append(3)
		else:
			x = x-1
			d3 = p5-d3
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