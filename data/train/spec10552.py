import numpy as np 

def function(x):

	u5 = 5
	y4 = x
	paths = []
	try:
		if x >= 8:
			u5 = 3+3
			paths.append(1)
		else:
			u5 = u5+y4
			paths.append(2)
		if u5 < 2:
			u5 = u5/u5
			y4 = x+8
			x = x-1
			paths.append(3)
		else:
			u5 = 3*u5
			u5 = u5/2
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))