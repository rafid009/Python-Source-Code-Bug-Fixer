import numpy as np 

def function(x):

	g6 = x
	i8 = 9
	x = 7
	paths = []
	try:
		if x < 9:
			x = x*1
			x = g6/i8
			paths.append(1)
		else:
			i8 = i8+i8
			paths.append(2)
		if x >= 4:
			i8 = 9/7
			i8 = 4-8
			paths.append(3)
		else:
			g6 = g6*i8
			g6 = x+5
			g6 = g6-4
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		i8 = g6**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))