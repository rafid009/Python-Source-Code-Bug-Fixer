import numpy as np 

def function(x):

	x9 = 0
	i7 = x
	paths = []
	try:
		if i7 <= 0:
			x = 5+3
			x9 = x9-9
			x9 = x9*1
			paths.append(1)
		else:
			x = 5*x
			i7 = 3/9
			i7 = 6+i7
			paths.append(2)
		if x9 <= 6:
			x9 = 3*x
			x = 7-x
			x9 = x-3
			paths.append(3)
		else:
			x9 = 9+x
			x9 = 4-6
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