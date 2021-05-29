import numpy as np 

def function(x):

	u7 = 2
	q9 = 2
	paths = []
	try:
		if q9 < 4:
			u7 = u7-3
			paths.append(1)
		else:
			u7 = 4-u7
			u7 = 2+u7
			paths.append(2)
		if q9 > 9:
			u7 = u7*9
			paths.append(3)
		else:
			q9 = 9*q9
			q9 = q9+q9
			u7 = q9+5
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