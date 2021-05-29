import numpy as np 

def function(x):

	g0 = x
	i6 = x
	paths = []
	try:
		if x <= 3:
			g0 = 7-1
			paths.append(1)
		else:
			g0 = 8*3
			paths.append(2)
		if x <= 2:
			x = 7+0
			paths.append(3)
		else:
			x = 3*x
			i6 = i6*g0
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))