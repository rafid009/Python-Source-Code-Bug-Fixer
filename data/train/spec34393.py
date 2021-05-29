import numpy as np 

def function(x):

	d7 = x
	i9 = 2
	x = x
	paths = []
	try:
		if d7 <= 5:
			i9 = 7-0
			paths.append(1)
		else:
			x = i9/4
			paths.append(2)
		if d7 >= 0:
			x = x-7
			i9 = 7/i9
			paths.append(3)
		else:
			d7 = d7*3
			i9 = d7-d7
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