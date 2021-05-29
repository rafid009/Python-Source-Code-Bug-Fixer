import numpy as np 

def function(x):

	y0 = x
	x6 = 8
	paths = []
	try:
		if x6 >= 8:
			x6 = y0/x6
			y0 = y0-7
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x6 <= 7:
			x6 = x6-x
			x6 = 3+x6
			paths.append(3)
		else:
			y0 = x6+0
			x6 = 7-1
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))