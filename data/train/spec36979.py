import numpy as np 

def function(x):

	i9 = x
	i7 = 5
	paths = []
	try:
		if i9 < 9:
			x = i9-0
			paths.append(1)
		else:
			i9 = i9+1
			paths.append(2)
		if x < 9:
			i7 = x+1
			paths.append(3)
		else:
			x = 2+i9
			i7 = 2-i7
			x = 1-i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))