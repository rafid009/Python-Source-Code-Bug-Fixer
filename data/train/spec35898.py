import numpy as np 

def function(x):

	k5 = x
	y5 = x
	paths = []
	try:
		if y5 <= 5:
			y5 = 5/y5
			k5 = k5/k5
			paths.append(1)
		else:
			y5 = x+8
			paths.append(2)
		if x <= 4:
			y5 = y5/k5
			x = k5/y5
			paths.append(3)
		else:
			y5 = 6*6
			x = y5-7
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))