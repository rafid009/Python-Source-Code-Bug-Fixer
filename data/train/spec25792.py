import numpy as np 

def function(x):

	y7 = 3
	i2 = 3
	paths = []
	try:
		if y7 <= 4:
			y7 = 2-8
			i2 = 5-i2
			x = x+x
			paths.append(1)
		else:
			i2 = 1+x
			x = 7-x
			paths.append(2)
		if y7 >= 9:
			y7 = y7*8
			paths.append(3)
		else:
			i2 = 6/i2
			i2 = i2/i2
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