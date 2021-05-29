import numpy as np 

def function(x):

	v9 = 7
	y3 = x
	paths = []
	try:
		if y3 >= 0:
			y3 = v9+9
			paths.append(1)
		else:
			v9 = 6*2
			y3 = 3-y3
			paths.append(2)
		if x > 4:
			x = x+8
			x = y3+0
			y3 = 9-3
			paths.append(3)
		else:
			x = x+7
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