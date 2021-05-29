import numpy as np 

def function(x):

	x4 = 2
	x8 = 0
	paths = []
	try:
		if x < 6:
			x8 = x8+x
			x4 = x4/1
			paths.append(1)
		else:
			x8 = x8+5
			x4 = x4+x4
			x8 = x8/2
			paths.append(2)
		if x4 <= 5:
			x8 = 4*x8
			x = x8-x
			paths.append(3)
		else:
			x8 = 7+x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))