import numpy as np 

def function(x):

	q6 = 8
	u4 = 9
	paths = []
	try:
		if x <= 1:
			x = u4*u4
			u4 = u4/8
			paths.append(1)
		else:
			u4 = x+u4
			paths.append(2)
		if x < 7:
			u4 = u4-4
			x = x+x
			paths.append(3)
		else:
			x = x/5
			q6 = 7-q6
			u4 = u4*q6
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