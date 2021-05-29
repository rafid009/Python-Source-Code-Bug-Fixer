import numpy as np 

def function(x):

	u5 = x
	u4 = 6
	paths = []
	try:
		if u5 > 4:
			u4 = u4*9
			u4 = 7+1
			x = x+x
			paths.append(1)
		else:
			u4 = u4*u5
			paths.append(2)
		if u5 < 9:
			u4 = 2/u4
			paths.append(3)
		else:
			u4 = 2/u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))