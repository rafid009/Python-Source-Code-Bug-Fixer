import numpy as np 

def function(x):

	y8 = x
	u7 = x
	paths = []
	try:
		if y8 <= 6:
			x = x-9
			paths.append(1)
		else:
			x = y8+4
			paths.append(2)
		if x <= 3:
			y8 = y8*8
			paths.append(3)
		else:
			u7 = u7+7
			x = x+x
			y8 = u7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))