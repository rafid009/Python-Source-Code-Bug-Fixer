import numpy as np 

def function(x):

	y1 = 1
	i3 = x
	paths = []
	try:
		if i3 >= 7:
			y1 = x+y1
			paths.append(1)
		else:
			y1 = y1-5
			i3 = i3-x
			y1 = y1-9
			paths.append(2)
		if x < 6:
			x = 9*x
			paths.append(3)
		else:
			i3 = 8-x
			y1 = y1-6
			x = x-i3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))