import numpy as np 

def function(x):

	i9 = 0
	y0 = 3
	paths = []
	try:
		if y0 <= 1:
			i9 = x-5
			x = x*2
			paths.append(1)
		else:
			x = 5-x
			y0 = y0+x
			x = 7-1
			paths.append(2)
		if i9 >= 5:
			i9 = 4-i9
			x = i9-x
			paths.append(3)
		else:
			i9 = 6-i9
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))