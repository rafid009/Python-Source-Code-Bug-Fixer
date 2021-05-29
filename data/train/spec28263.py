import numpy as np 

def function(x):

	y5 = x
	y2 = 0
	paths = []
	try:
		if x <= 1:
			y2 = x-y2
			y5 = y5+5
			y5 = y5*4
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x >= 2:
			y2 = y2+9
			y2 = y2/2
			x = x-0
			paths.append(3)
		else:
			y2 = 1*x
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y2 = y5**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))