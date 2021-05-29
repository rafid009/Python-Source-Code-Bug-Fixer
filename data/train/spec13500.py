import numpy as np 

def function(x):

	i9 = x
	c4 = x
	paths = []
	try:
		if i9 >= 2:
			i9 = x/8
			x = x-5
			x = x-2
			paths.append(1)
		else:
			i9 = i9+0
			paths.append(2)
		if x <= 9:
			i9 = 1-i9
			i9 = i9*2
			i9 = 9-i9
			paths.append(3)
		else:
			i9 = i9/9
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))