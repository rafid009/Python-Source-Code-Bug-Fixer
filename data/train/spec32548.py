import numpy as np 

def function(x):

	u7 = x
	paths = []
	try:
		if x > 8:
			u7 = u7-0
			paths.append(1)
		else:
			u7 = 4*u7
			u7 = x/8
			u7 = u7/6
			paths.append(2)
		if u7 > 4:
			u7 = 7*u7
			u7 = 9/u7
			x = 6-1
			paths.append(3)
		else:
			u7 = x*u7
			x = x+6
			u7 = 7*u7
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