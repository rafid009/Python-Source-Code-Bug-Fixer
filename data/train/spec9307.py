import numpy as np 

def function(x):

	i7 = x
	a7 = x
	paths = []
	try:
		if i7 >= 2:
			i7 = a7+4
			i7 = i7/x
			paths.append(1)
		else:
			i7 = i7-x
			i7 = a7*x
			paths.append(2)
		if i7 <= 1:
			x = x-a7
			i7 = i7+7
			paths.append(3)
		else:
			x = i7+x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))