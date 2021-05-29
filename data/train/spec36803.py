import numpy as np 

def function(x):

	x8 = 9
	b8 = x
	x = 7
	paths = []
	try:
		if x < 6:
			x8 = 9/x8
			x = x/x
			x = 0/x
			paths.append(1)
		else:
			x = 6+x
			x8 = 0-1
			x8 = x8/b8
			paths.append(2)
		if x8 >= 7:
			x = 3-x
			x8 = x8*1
			paths.append(3)
		else:
			x = 3+x
			x8 = x8/3
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))