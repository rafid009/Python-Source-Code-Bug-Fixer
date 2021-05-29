import numpy as np 

def function(x):

	y7 = x
	u6 = x
	paths = []
	try:
		if u6 < 0:
			u6 = 5-y7
			y7 = 7/x
			y7 = y7+y7
			paths.append(1)
		else:
			y7 = y7-6
			u6 = 0+0
			paths.append(2)
		if y7 > 4:
			y7 = 8/2
			paths.append(3)
		else:
			u6 = u6/1
			y7 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))