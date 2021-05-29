import numpy as np 

def function(x):

	g9 = 6
	i8 = x
	x = 7
	paths = []
	try:
		if g9 >= 3:
			x = 7*x
			i8 = i8*9
			x = x/g9
			paths.append(1)
		else:
			g9 = g9*3
			paths.append(2)
		if i8 >= 1:
			x = 0-7
			x = x-x
			x = x+9
			paths.append(3)
		else:
			x = 3+x
			x = x-1
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