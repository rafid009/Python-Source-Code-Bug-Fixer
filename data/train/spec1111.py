import numpy as np 

def function(x):

	y8 = 5
	k1 = x
	paths = []
	try:
		if y8 > 1:
			y8 = 0+9
			y8 = 6/2
			paths.append(1)
		else:
			x = 4/y8
			x = 2+y8
			k1 = k1-1
			paths.append(2)
		if k1 >= 4:
			k1 = 3*k1
			y8 = 4*y8
			y8 = x*6
			paths.append(3)
		else:
			x = 9/8
			y8 = 1-y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))