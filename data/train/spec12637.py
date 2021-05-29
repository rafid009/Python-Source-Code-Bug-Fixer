import numpy as np 

def function(x):

	x2 = 6
	i5 = x
	paths = []
	try:
		if x2 >= 8:
			x2 = 7-6
			x2 = 3/x2
			paths.append(1)
		else:
			i5 = i5-x
			i5 = i5+4
			paths.append(2)
		if x2 > 5:
			x2 = x2-7
			paths.append(3)
		else:
			i5 = 2-i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))