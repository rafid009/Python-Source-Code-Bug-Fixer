import numpy as np 

def function(x):

	y8 = 8
	r5 = x
	paths = []
	try:
		if r5 < 6:
			y8 = 5/x
			y8 = y8+3
			x = 6+x
			paths.append(1)
		else:
			x = 0-x
			y8 = y8-x
			paths.append(2)
		if x > 5:
			x = 4+0
			paths.append(3)
		else:
			y8 = 9-y8
			x = r5-x
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