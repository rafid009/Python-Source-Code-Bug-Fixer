import numpy as np 

def function(x):

	d7 = 4
	y1 = x
	x = 7
	paths = []
	try:
		if d7 <= 0:
			d7 = d7*x
			d7 = 7-d7
			paths.append(1)
		else:
			y1 = y1+1
			paths.append(2)
		if x > 8:
			x = d7-x
			d7 = d7-d7
			paths.append(3)
		else:
			x = y1/x
			d7 = d7+x
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))