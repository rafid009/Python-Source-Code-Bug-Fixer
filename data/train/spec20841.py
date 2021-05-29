import numpy as np 

def function(x):

	g3 = 3
	i0 = x
	paths = []
	try:
		if x < 2:
			x = 8/x
			x = x+i0
			x = 5-x
			paths.append(1)
		else:
			x = 7+4
			paths.append(2)
		if g3 < 1:
			i0 = i0+3
			paths.append(3)
		else:
			g3 = g3-i0
			g3 = g3*4
			g3 = i0+g3
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))