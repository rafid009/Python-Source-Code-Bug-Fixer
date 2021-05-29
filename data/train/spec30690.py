import numpy as np 

def function(x):

	x8 = 8
	u9 = x
	paths = []
	try:
		if x < 0:
			x = x/u9
			paths.append(1)
		else:
			x = x8-1
			x8 = x8+x8
			u9 = 3/u9
			paths.append(2)
		if x <= 6:
			u9 = 2*u9
			x8 = x8*6
			paths.append(3)
		else:
			x = 8/u9
			x8 = 5/u9
			x = 9*u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))