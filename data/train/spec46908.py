import numpy as np 

def function(x):

	y8 = x
	i7 = 8
	paths = []
	try:
		if i7 >= 8:
			y8 = y8/x
			i7 = i7+6
			x = 1+x
			paths.append(1)
		else:
			i7 = i7-2
			paths.append(2)
		if y8 <= 5:
			y8 = i7+y8
			paths.append(3)
		else:
			x = x/3
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