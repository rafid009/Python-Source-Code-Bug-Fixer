import numpy as np 

def function(x):

	y8 = x
	i3 = x
	paths = []
	try:
		if x >= 6:
			y8 = y8*y8
			i3 = i3/i3
			paths.append(1)
		else:
			x = y8*9
			x = 5-x
			paths.append(2)
		if i3 <= 6:
			y8 = 5+y8
			i3 = i3+y8
			paths.append(3)
		else:
			x = 1/6
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		y8 = i3**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))