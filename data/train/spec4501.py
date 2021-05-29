import numpy as np 

def function(x):

	y2 = x
	x9 = x
	paths = []
	try:
		if x9 <= 3:
			x = x9+x
			paths.append(1)
		else:
			y2 = x9/8
			paths.append(2)
		if x < 8:
			x9 = x9-0
			x = x*9
			paths.append(3)
		else:
			x9 = x9+x9
			x = x/y2
			x9 = x9-7
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		y2 = x9**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))