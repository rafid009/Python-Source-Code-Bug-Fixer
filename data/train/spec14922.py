import numpy as np 

def function(x):

	i4 = 5
	g4 = x
	paths = []
	try:
		if i4 < 1:
			g4 = g4+g4
			g4 = g4/8
			paths.append(1)
		else:
			x = i4/x
			paths.append(2)
		if x < 6:
			x = 1+3
			x = x*6
			paths.append(3)
		else:
			g4 = g4-3
			i4 = 2+3
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		i4 = g4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))