import numpy as np 

def function(x):

	a7 = 9
	y7 = x
	paths = []
	try:
		if x >= 0:
			x = 0+x
			y7 = y7+3
			paths.append(1)
		else:
			a7 = 1-a7
			a7 = x-a7
			y7 = x/7
			paths.append(2)
		if x < 9:
			x = 6*y7
			y7 = 9+9
			paths.append(3)
		else:
			a7 = x-9
			a7 = a7+0
			y7 = 5+1
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		y7 = a7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))