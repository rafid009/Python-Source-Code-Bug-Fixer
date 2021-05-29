import numpy as np 

def function(x):

	u5 = 9
	u2 = 4
	paths = []
	try:
		if x < 1:
			u5 = u2-u5
			u5 = u5-8
			u2 = 0-3
			paths.append(1)
		else:
			x = x*7
			x = x-7
			x = 6+0
			paths.append(2)
		if u5 > 2:
			u5 = u5+u5
			x = u5+5
			u5 = u5-7
			paths.append(3)
		else:
			u5 = 6/u5
			x = x*7
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))