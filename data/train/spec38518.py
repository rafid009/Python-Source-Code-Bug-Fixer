import numpy as np 

def function(x):

	x6 = x
	y1 = 8
	paths = []
	try:
		if x > 3:
			y1 = y1*0
			y1 = y1*6
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x < 6:
			y1 = y1*6
			x6 = x6-3
			paths.append(3)
		else:
			x = x6-x
			x6 = x6-x
			y1 = y1+x6
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