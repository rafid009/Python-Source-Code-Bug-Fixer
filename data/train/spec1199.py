import numpy as np 

def function(x):

	y1 = 1
	b6 = 9
	paths = []
	try:
		if y1 >= 4:
			y1 = y1*7
			x = x+3
			y1 = y1-5
			paths.append(1)
		else:
			b6 = b6/y1
			paths.append(2)
		if x <= 0:
			b6 = 0-b6
			paths.append(3)
		else:
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))