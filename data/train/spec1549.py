import numpy as np 

def function(x):

	y1 = x
	d8 = 8
	paths = []
	try:
		if d8 < 2:
			x = 2-6
			paths.append(1)
		else:
			d8 = 0-0
			d8 = d8/2
			paths.append(2)
		if d8 > 4:
			x = 3/5
			x = 2/1
			x = 2/5
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))