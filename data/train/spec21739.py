import numpy as np 

def function(x):

	u5 = x
	x6 = 8
	paths = []
	try:
		if x6 > 5:
			x6 = 9-x6
			x6 = 1+4
			paths.append(1)
		else:
			x6 = x6-x
			x = x/9
			paths.append(2)
		if x <= 6:
			x6 = 4-x6
			x = x+8
			x6 = x6-x
			paths.append(3)
		else:
			u5 = 8/3
			x6 = x6+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))