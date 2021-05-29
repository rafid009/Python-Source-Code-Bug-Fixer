import numpy as np 

def function(x):

	a8 = 9
	i7 = 9
	paths = []
	try:
		if x <= 9:
			i7 = i7*8
			paths.append(1)
		else:
			a8 = 0-a8
			paths.append(2)
		if i7 > 9:
			a8 = 9/8
			paths.append(3)
		else:
			a8 = 9-a8
			x = 4-x
			i7 = x-i7
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