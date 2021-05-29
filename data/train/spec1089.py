import numpy as np 

def function(x):

	x8 = 1
	y3 = x
	paths = []
	try:
		if y3 >= 0:
			y3 = 4+7
			y3 = 7-y3
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x < 7:
			x = 3+x
			x8 = 4-x8
			y3 = y3+2
			paths.append(3)
		else:
			x8 = x8/9
			y3 = 1*8
			x = x/x8
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