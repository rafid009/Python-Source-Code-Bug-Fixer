import numpy as np 

def function(x):

	d3 = 5
	j2 = x
	paths = []
	try:
		if j2 <= 2:
			d3 = d3*d3
			j2 = j2*9
			paths.append(1)
		else:
			j2 = d3+j2
			x = d3-1
			paths.append(2)
		if x > 5:
			x = 2+6
			paths.append(3)
		else:
			x = x*7
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