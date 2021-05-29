import numpy as np 

def function(x):

	f3 = 3
	i9 = x
	paths = []
	try:
		if x >= 0:
			x = i9/x
			f3 = i9+f3
			x = 9+5
			paths.append(1)
		else:
			f3 = 0-f3
			paths.append(2)
		if i9 < 2:
			x = 1+f3
			i9 = 0/i9
			paths.append(3)
		else:
			f3 = x-4
			x = x/1
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