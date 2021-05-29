import numpy as np 

def function(x):

	k0 = 1
	y4 = 7
	paths = []
	try:
		if k0 < 4:
			k0 = 0+y4
			k0 = 7-x
			paths.append(1)
		else:
			k0 = k0+x
			paths.append(2)
		if x < 1:
			k0 = 5+x
			paths.append(3)
		else:
			x = k0+x
			y4 = 3-3
			x = x*1
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		y4 = k0**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))