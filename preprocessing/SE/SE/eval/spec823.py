import numpy as np 

def function(x):

	y8 = x
	u9 = x
	paths = []
	try:
		if y8 <= 5:
			y8 = u9-4
			u9 = x+y8
			u9 = x*9
			paths.append(1)
		else:
			u9 = u9*6
			u9 = u9-u9
			y8 = 2*3
			paths.append(2)
		if x <= 5:
			y8 = 7-y8
			paths.append(3)
		else:
			u9 = u9+7
			u9 = y8*4
			u9 = y8-0
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		y8 = u9**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))