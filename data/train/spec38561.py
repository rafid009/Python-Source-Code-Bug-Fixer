import numpy as np 

def function(x):

	u7 = 8
	y2 = 1
	paths = []
	try:
		if x >= 8:
			x = x-6
			y2 = y2-2
			paths.append(1)
		else:
			y2 = 7*2
			x = x/8
			u7 = u7/u7
			paths.append(2)
		if u7 >= 9:
			y2 = y2+x
			paths.append(3)
		else:
			u7 = 3/u7
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))