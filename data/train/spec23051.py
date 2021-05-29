import numpy as np 

def function(x):

	a4 = x
	i7 = 2
	paths = []
	try:
		if x >= 2:
			a4 = 8+i7
			x = x/x
			i7 = 0+a4
			paths.append(1)
		else:
			i7 = i7+i7
			x = x/x
			paths.append(2)
		if i7 <= 1:
			i7 = 8-0
			paths.append(3)
		else:
			i7 = i7-7
			a4 = a4-x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))