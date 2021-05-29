import numpy as np 

def function(x):

	i0 = x
	g3 = x
	paths = []
	try:
		if x < 3:
			g3 = i0/5
			paths.append(1)
		else:
			i0 = 3/i0
			g3 = 8*i0
			paths.append(2)
		if g3 >= 5:
			i0 = i0/2
			i0 = i0-g3
			x = i0-x
			paths.append(3)
		else:
			i0 = 9-i0
			x = 3+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))