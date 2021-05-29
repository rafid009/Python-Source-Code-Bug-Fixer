import numpy as np 

def function(x):

	y3 = 1
	u2 = x
	paths = []
	try:
		if u2 >= 3:
			u2 = u2-u2
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if y3 < 1:
			y3 = y3*8
			paths.append(3)
		else:
			u2 = 4/x
			u2 = 5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))