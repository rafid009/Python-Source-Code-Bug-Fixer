import numpy as np 

def function(x):

	e5 = x
	d5 = 6
	paths = []
	try:
		if e5 >= 8:
			x = 9-x
			x = 4*x
			d5 = 1/2
			paths.append(1)
		else:
			x = x-d5
			paths.append(2)
		if d5 > 5:
			x = x/x
			paths.append(3)
		else:
			e5 = 5/x
			d5 = d5-1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		d5 = e5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))