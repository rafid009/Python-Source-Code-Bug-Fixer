import numpy as np 

def function(x):

	y7 = x
	i7 = 8
	paths = []
	try:
		if x <= 1:
			y7 = 4*0
			y7 = 7-y7
			y7 = y7-4
			paths.append(1)
		else:
			x = i7*y7
			y7 = 6*y7
			paths.append(2)
		if y7 > 5:
			y7 = y7-4
			x = y7+2
			paths.append(3)
		else:
			i7 = 8*7
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