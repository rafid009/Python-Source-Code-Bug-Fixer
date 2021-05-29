import numpy as np 

def function(x):

	a6 = x
	i9 = x
	paths = []
	try:
		if x > 2:
			x = i9*1
			i9 = x*3
			i9 = x/3
			paths.append(1)
		else:
			x = x*6
			x = x+0
			a6 = 1-x
			paths.append(2)
		if i9 <= 2:
			i9 = i9+1
			paths.append(3)
		else:
			i9 = 8-i9
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