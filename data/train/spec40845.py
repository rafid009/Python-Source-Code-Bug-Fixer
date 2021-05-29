import numpy as np 

def function(x):

	i8 = 0
	y4 = x
	x = x
	paths = []
	try:
		if i8 <= 8:
			y4 = y4-6
			x = x*4
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if i8 <= 9:
			i8 = 5+y4
			paths.append(3)
		else:
			x = 5+x
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))