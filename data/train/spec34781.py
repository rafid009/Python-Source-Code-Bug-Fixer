import numpy as np 

def function(x):

	u4 = x
	q8 = 4
	paths = []
	try:
		if q8 <= 6:
			u4 = 9/u4
			q8 = q8/1
			paths.append(1)
		else:
			q8 = 6+9
			q8 = q8*q8
			x = 5/9
			paths.append(2)
		if q8 >= 0:
			q8 = q8-q8
			x = 7-5
			paths.append(3)
		else:
			u4 = 9/q8
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))