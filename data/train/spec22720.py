import numpy as np 

def function(x):

	y7 = x
	b9 = 7
	paths = []
	try:
		if y7 > 2:
			y7 = y7-0
			y7 = y7+0
			x = x+9
			paths.append(1)
		else:
			x = x+8
			y7 = x/1
			y7 = 1+y7
			paths.append(2)
		if y7 <= 1:
			x = 9/x
			paths.append(3)
		else:
			y7 = y7/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))