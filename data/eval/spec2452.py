import numpy as np 

def function(x):

	y6 = x
	y1 = 5
	paths = []
	try:
		if x <= 3:
			x = y1/x
			x = 1*x
			y6 = y6*4
			paths.append(1)
		else:
			y1 = 3*3
			y1 = y1-y1
			y1 = y1-y1
			paths.append(2)
		if y6 < 2:
			x = x*9
			y6 = y6*y1
			x = y1/x
			paths.append(3)
		else:
			y1 = x*0
			y6 = y1/8
			x = x+y6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))