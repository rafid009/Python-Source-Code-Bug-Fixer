import numpy as np 

def function(x):

	c5 = 5
	u9 = 0
	paths = []
	try:
		if x <= 6:
			x = 5*x
			u9 = 9*3
			u9 = 1/u9
			paths.append(1)
		else:
			u9 = u9-6
			x = 1*4
			paths.append(2)
		if x < 3:
			u9 = 3-2
			u9 = 1+u9
			paths.append(3)
		else:
			x = 5-1
			x = x+u9
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