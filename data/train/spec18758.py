import numpy as np 

def function(x):

	i8 = 5
	g5 = 4
	x = 2
	paths = []
	try:
		if g5 < 9:
			g5 = 6-g5
			i8 = g5+i8
			paths.append(1)
		else:
			x = i8/4
			i8 = i8+0
			paths.append(2)
		if x <= 8:
			i8 = 3-4
			g5 = 3/4
			paths.append(3)
		else:
			g5 = 0*g5
			g5 = g5/4
			i8 = i8*i8
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