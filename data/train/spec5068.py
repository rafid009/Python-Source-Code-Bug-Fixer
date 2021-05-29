import numpy as np 

def function(x):

	y4 = 7
	x3 = 3
	paths = []
	try:
		if x > 3:
			y4 = 0-5
			x = 5-9
			paths.append(1)
		else:
			x3 = 4-x3
			x = x*x3
			paths.append(2)
		if y4 >= 4:
			x = 4*0
			x3 = x3/x3
			y4 = x*y4
			paths.append(3)
		else:
			y4 = x*x3
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))