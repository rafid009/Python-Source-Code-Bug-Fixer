import numpy as np 

def function(x):

	k7 = 0
	y6 = 1
	paths = []
	try:
		if k7 < 8:
			x = x-9
			paths.append(1)
		else:
			k7 = 1/6
			k7 = k7*x
			x = x+0
			paths.append(2)
		if y6 <= 4:
			y6 = y6*6
			k7 = k7*9
			paths.append(3)
		else:
			k7 = y6-7
			y6 = y6-0
			x = x/8
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