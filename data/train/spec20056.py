import numpy as np 

def function(x):

	i7 = x
	y7 = x
	paths = []
	try:
		if x >= 1:
			y7 = y7*5
			i7 = 9-i7
			paths.append(1)
		else:
			x = i7-1
			i7 = i7-x
			paths.append(2)
		if i7 <= 4:
			i7 = 1-i7
			paths.append(3)
		else:
			x = i7*x
			y7 = 4*6
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))