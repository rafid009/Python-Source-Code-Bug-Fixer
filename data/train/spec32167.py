import numpy as np 

def function(x):

	y1 = 3
	i6 = 7
	paths = []
	try:
		if y1 >= 1:
			i6 = 3+x
			x = x*3
			i6 = y1-i6
			paths.append(1)
		else:
			i6 = i6+6
			paths.append(2)
		if y1 > 0:
			i6 = i6+7
			x = x/5
			i6 = 2/x
			paths.append(3)
		else:
			y1 = y1-5
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