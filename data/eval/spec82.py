import numpy as np 

def function(x):

	y1 = x
	x3 = x
	x = x
	paths = []
	try:
		if x3 <= 3:
			x3 = x3*3
			paths.append(1)
		else:
			y1 = y1/9
			x3 = x3*x3
			x3 = x3*6
			paths.append(2)
		if x >= 4:
			y1 = y1+y1
			y1 = y1*x
			y1 = 6*1
			paths.append(3)
		else:
			y1 = y1/2
			x = x3+x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))