import numpy as np 

def function(x):

	q7 = 1
	u8 = 6
	paths = []
	try:
		if x > 9:
			x = u8-8
			u8 = 6-u8
			paths.append(1)
		else:
			x = u8+x
			paths.append(2)
		if u8 > 2:
			q7 = 4*q7
			q7 = 3/q7
			paths.append(3)
		else:
			u8 = q7+x
			q7 = q7/u8
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))