import numpy as np 

def function(x):

	d3 = 6
	r4 = x
	paths = []
	try:
		if x < 3:
			r4 = r4*0
			x = 9*x
			x = 9+x
			paths.append(1)
		else:
			d3 = 7+0
			paths.append(2)
		if d3 >= 2:
			r4 = r4+6
			paths.append(3)
		else:
			r4 = 5/r4
			d3 = x+1
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