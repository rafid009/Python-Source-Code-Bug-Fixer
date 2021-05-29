import numpy as np 

def function(x):

	y4 = 5
	k0 = 5
	paths = []
	try:
		if x > 8:
			k0 = y4+7
			paths.append(1)
		else:
			y4 = y4*6
			x = x+x
			y4 = y4/8
			paths.append(2)
		if k0 > 8:
			y4 = y4*0
			y4 = k0-7
			paths.append(3)
		else:
			y4 = 9*y4
			k0 = 7+x
			k0 = k0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))