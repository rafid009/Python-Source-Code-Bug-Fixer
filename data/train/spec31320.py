import numpy as np 

def function(x):

	r1 = x
	y1 = 6
	paths = []
	try:
		if r1 >= 6:
			x = 6-r1
			x = x*x
			y1 = y1-y1
			paths.append(1)
		else:
			y1 = 9/y1
			y1 = 0*y1
			y1 = y1*6
			paths.append(2)
		if x <= 1:
			x = 7/7
			paths.append(3)
		else:
			y1 = 4-y1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		y1 = r1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))