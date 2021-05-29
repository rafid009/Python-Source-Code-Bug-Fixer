import numpy as np 

def function(x):

	q4 = x
	u7 = x
	paths = []
	try:
		if u7 < 9:
			x = 4*q4
			paths.append(1)
		else:
			x = 8-x
			u7 = q4*7
			paths.append(2)
		if q4 > 8:
			q4 = u7-q4
			q4 = q4/4
			x = q4/1
			paths.append(3)
		else:
			q4 = q4-q4
			u7 = 4*9
			u7 = u7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))