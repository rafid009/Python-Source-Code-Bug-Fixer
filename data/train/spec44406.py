import numpy as np 

def function(x):

	d7 = 1
	x0 = x
	paths = []
	try:
		if x < 7:
			x0 = 5-x0
			d7 = d7+x0
			paths.append(1)
		else:
			x0 = x0+d7
			x0 = x0/9
			paths.append(2)
		if d7 > 7:
			d7 = 8-d7
			paths.append(3)
		else:
			d7 = x/4
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))