import numpy as np 

def function(x):

	i5 = x
	y1 = 1
	paths = []
	try:
		if y1 > 6:
			x = 0-8
			y1 = y1-y1
			paths.append(1)
		else:
			y1 = y1*9
			x = 9-8
			paths.append(2)
		if x < 5:
			x = x*i5
			y1 = x/1
			paths.append(3)
		else:
			x = x-5
			x = x*3
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		y1 = i5**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))