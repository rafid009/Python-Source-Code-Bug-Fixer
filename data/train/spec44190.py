import numpy as np 

def function(x):

	y3 = x
	u2 = x
	paths = []
	try:
		if x >= 1:
			x = 3*u2
			paths.append(1)
		else:
			x = y3*2
			paths.append(2)
		if y3 < 2:
			u2 = x*x
			y3 = 4-u2
			u2 = u2-x
			paths.append(3)
		else:
			x = u2/5
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))