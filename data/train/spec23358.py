import numpy as np 

def function(x):

	y7 = 5
	y3 = x
	paths = []
	try:
		if y7 <= 6:
			y7 = 2/y7
			y7 = x-9
			y3 = y3-0
			paths.append(1)
		else:
			y3 = 4+y7
			paths.append(2)
		if x > 3:
			y3 = x*x
			y7 = y7-x
			x = 6+2
			paths.append(3)
		else:
			x = x-x
			y7 = 9+y7
			y7 = y7*x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y7 = y3**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))