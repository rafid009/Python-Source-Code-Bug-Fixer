import numpy as np 

def function(x):

	x0 = x
	d8 = 2
	paths = []
	try:
		if x0 >= 9:
			x0 = 5/x0
			x0 = d8*0
			d8 = d8*x
			paths.append(1)
		else:
			x0 = x0*x
			x0 = x0/x0
			paths.append(2)
		if x > 1:
			x = 6-x
			x0 = 7+x0
			x0 = 0+x0
			paths.append(3)
		else:
			d8 = 3*x0
			d8 = 1-d8
			x = 6*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))