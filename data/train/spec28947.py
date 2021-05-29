import numpy as np 

def function(x):

	k5 = x
	y8 = 1
	paths = []
	try:
		if x >= 7:
			x = 9/x
			x = 4*2
			y8 = y8-k5
			paths.append(1)
		else:
			k5 = k5-6
			y8 = y8-8
			paths.append(2)
		if x > 1:
			x = x-6
			y8 = 7+k5
			x = k5*4
			paths.append(3)
		else:
			y8 = y8-5
			y8 = y8+k5
			y8 = 6*y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))