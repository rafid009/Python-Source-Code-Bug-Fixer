import numpy as np 

def function(x):

	y1 = 8
	n7 = x
	paths = []
	try:
		if y1 <= 4:
			n7 = 3+8
			n7 = 7*5
			paths.append(1)
		else:
			y1 = y1+5
			y1 = y1+x
			y1 = x+x
			paths.append(2)
		if n7 >= 6:
			x = 8+x
			paths.append(3)
		else:
			x = x-3
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