import numpy as np 

def function(x):

	y5 = x
	d1 = x
	paths = []
	try:
		if x > 9:
			x = x/2
			paths.append(1)
		else:
			d1 = y5*7
			x = 3-0
			paths.append(2)
		if y5 >= 3:
			d1 = d1*y5
			paths.append(3)
		else:
			x = d1/1
			y5 = y5+y5
			y5 = 8/y5
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))