import numpy as np 

def function(x):

	d7 = 4
	r7 = 0
	paths = []
	try:
		if x > 4:
			d7 = 8-d7
			x = x/6
			paths.append(1)
		else:
			x = d7/2
			paths.append(2)
		if x >= 6:
			d7 = d7+x
			paths.append(3)
		else:
			x = 1-9
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))