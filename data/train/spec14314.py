import numpy as np 

def function(x):

	i9 = 2
	k2 = 2
	x = 5
	paths = []
	try:
		if x <= 8:
			i9 = x-i9
			paths.append(1)
		else:
			k2 = k2+1
			paths.append(2)
		if k2 < 0:
			x = 8/i9
			i9 = 2+i9
			i9 = i9*4
			paths.append(3)
		else:
			x = 7+x
			k2 = k2+7
			x = i9-4
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