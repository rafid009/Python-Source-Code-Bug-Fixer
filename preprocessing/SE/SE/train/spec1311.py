import numpy as np 

def function(x):

	d4 = 3
	y1 = 7
	paths = []
	try:
		if y1 >= 0:
			d4 = 3*0
			y1 = 3*4
			paths.append(1)
		else:
			y1 = y1/1
			paths.append(2)
		if x <= 2:
			y1 = y1/x
			x = x+0
			paths.append(3)
		else:
			y1 = x*y1
			d4 = y1/x
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))