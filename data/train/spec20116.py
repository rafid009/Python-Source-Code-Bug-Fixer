import numpy as np 

def function(x):

	u4 = 8
	x6 = 9
	paths = []
	try:
		if x <= 7:
			u4 = 3-u4
			x6 = 0+x6
			x6 = x6-6
			paths.append(1)
		else:
			x6 = 7/6
			x6 = 2+x6
			paths.append(2)
		if u4 < 6:
			x = x-4
			paths.append(3)
		else:
			x6 = 3-x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		u4 = x6**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))