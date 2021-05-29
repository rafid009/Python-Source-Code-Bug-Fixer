import numpy as np 

def function(x):

	j7 = 4
	d3 = x
	paths = []
	try:
		if j7 < 4:
			d3 = d3+7
			d3 = j7*d3
			d3 = 9*2
			paths.append(1)
		else:
			d3 = 8*d3
			paths.append(2)
		if d3 <= 7:
			j7 = j7*4
			paths.append(3)
		else:
			d3 = d3/6
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