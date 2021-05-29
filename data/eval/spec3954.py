import numpy as np 

def function(x):

	i9 = x
	y1 = x
	paths = []
	try:
		if y1 <= 3:
			x = x/y1
			i9 = i9/x
			paths.append(1)
		else:
			y1 = 7-8
			x = y1-2
			paths.append(2)
		if i9 >= 2:
			x = y1/2
			x = 3*x
			i9 = i9+3
			paths.append(3)
		else:
			x = y1*x
			x = y1+x
			y1 = y1*y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		i9 = y1**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))