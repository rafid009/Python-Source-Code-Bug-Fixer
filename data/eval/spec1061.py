import numpy as np 

def function(x):

	u7 = 0
	d6 = 6
	paths = []
	try:
		if x <= 0:
			d6 = 8*d6
			u7 = 8+7
			paths.append(1)
		else:
			d6 = x+d6
			x = x+5
			d6 = u7*d6
			paths.append(2)
		if x < 6:
			x = x-2
			u7 = u7*d6
			u7 = 5/x
			paths.append(3)
		else:
			u7 = 6-3
			u7 = u7*u7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))