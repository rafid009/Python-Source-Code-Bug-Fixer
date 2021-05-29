import numpy as np 

def function(x):

	k0 = 5
	y4 = 3
	paths = []
	try:
		if x > 9:
			y4 = y4*3
			y4 = x*x
			paths.append(1)
		else:
			x = 4/x
			k0 = k0+x
			x = 4-x
			paths.append(2)
		if y4 >= 6:
			x = k0-y4
			x = x+3
			k0 = 6*k0
			paths.append(3)
		else:
			y4 = y4-6
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))