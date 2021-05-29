import numpy as np 

def function(x):

	u7 = x
	m8 = 9
	x = x
	paths = []
	try:
		if x <= 5:
			x = x-6
			x = 7*x
			x = 7+u7
			paths.append(1)
		else:
			u7 = 3-u7
			u7 = u7+0
			u7 = u7/6
			paths.append(2)
		if x > 6:
			m8 = 5/x
			x = u7*x
			u7 = 2/u7
			paths.append(3)
		else:
			x = 9+x
			u7 = 7+u7
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