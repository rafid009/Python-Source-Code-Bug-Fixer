import numpy as np 

def function(x):

	q6 = 3
	u7 = 9
	paths = []
	try:
		if u7 <= 5:
			u7 = u7*9
			q6 = q6*x
			paths.append(1)
		else:
			q6 = q6-2
			u7 = u7-x
			q6 = x*8
			paths.append(2)
		if q6 < 2:
			u7 = x*u7
			paths.append(3)
		else:
			q6 = u7/6
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