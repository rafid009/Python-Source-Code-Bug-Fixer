import numpy as np 

def function(x):

	y1 = x
	x2 = 4
	x = 5
	paths = []
	try:
		if y1 <= 3:
			x = 6-x
			x2 = y1*9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x2 < 0:
			y1 = y1/y1
			paths.append(3)
		else:
			x = 5-2
			x2 = x-x2
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))