import numpy as np 

def function(x):

	f3 = x
	d3 = x
	paths = []
	try:
		if x < 1:
			f3 = f3*x
			paths.append(1)
		else:
			x = 5*4
			paths.append(2)
		if f3 >= 9:
			f3 = 2-f3
			f3 = 3/4
			d3 = x-x
			paths.append(3)
		else:
			f3 = 2+x
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