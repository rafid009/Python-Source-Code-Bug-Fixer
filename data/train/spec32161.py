import numpy as np 

def function(x):

	g7 = 9
	v7 = x
	paths = []
	try:
		if g7 >= 6:
			v7 = v7-5
			paths.append(1)
		else:
			v7 = v7-5
			v7 = 0+v7
			paths.append(2)
		if g7 > 3:
			v7 = v7+g7
			x = 0/x
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))