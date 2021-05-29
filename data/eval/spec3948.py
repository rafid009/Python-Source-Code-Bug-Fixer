import numpy as np 

def function(x):

	y3 = 8
	u9 = x
	paths = []
	try:
		if x <= 6:
			y3 = y3+3
			paths.append(1)
		else:
			x = y3+y3
			paths.append(2)
		if x <= 4:
			x = x/4
			u9 = u9/2
			y3 = y3*y3
			paths.append(3)
		else:
			y3 = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))