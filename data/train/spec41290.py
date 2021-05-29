import numpy as np 

def function(x):

	b6 = 8
	d3 = x
	paths = []
	try:
		if b6 <= 4:
			d3 = 3+5
			d3 = d3/2
			b6 = b6+5
			paths.append(1)
		else:
			b6 = 7/b6
			d3 = d3*x
			paths.append(2)
		if x < 7:
			b6 = d3+x
			paths.append(3)
		else:
			d3 = 3/2
			b6 = b6/6
			b6 = b6/9
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