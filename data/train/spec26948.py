import numpy as np 

def function(x):

	x4 = 9
	i7 = x
	paths = []
	try:
		if x4 > 2:
			i7 = i7+4
			x4 = i7-x4
			paths.append(1)
		else:
			i7 = i7*6
			x = 5-x
			paths.append(2)
		if i7 >= 3:
			x4 = x4/5
			paths.append(3)
		else:
			x = i7-x
			x = 8*3
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x4 = i7**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))