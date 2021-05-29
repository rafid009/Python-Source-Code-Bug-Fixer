import numpy as np 

def function(x):

	d7 = 2
	o2 = 7
	paths = []
	try:
		if x < 4:
			x = x-8
			x = o2*x
			paths.append(1)
		else:
			d7 = d7-1
			paths.append(2)
		if d7 <= 2:
			d7 = d7-x
			x = 1-x
			d7 = 0*4
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))