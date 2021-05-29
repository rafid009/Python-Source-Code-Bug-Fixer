import numpy as np 

def function(x):

	y3 = 6
	paths = []
	try:
		if y3 <= 8:
			y3 = 1+y3
			paths.append(1)
		else:
			y3 = 7+9
			paths.append(2)
		if x < 9:
			x = 7/7
			paths.append(3)
		else:
			y3 = 4-y3
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))