import numpy as np 

def function(x):

	y6 = 3
	i9 = x
	paths = []
	try:
		if i9 > 4:
			y6 = y6+y6
			x = 4-x
			y6 = y6-5
			paths.append(1)
		else:
			i9 = 6/4
			x = 9*0
			paths.append(2)
		if i9 >= 8:
			x = x/1
			y6 = i9+y6
			paths.append(3)
		else:
			i9 = i9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))