import numpy as np 

def function(x):

	q2 = 4
	y0 = 8
	paths = []
	try:
		if x <= 2:
			q2 = q2*0
			paths.append(1)
		else:
			q2 = q2*y0
			paths.append(2)
		if x < 1:
			y0 = x-3
			paths.append(3)
		else:
			x = 2-0
			x = x+0
			q2 = 1/3
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))