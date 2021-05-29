import numpy as np 

def function(x):

	u7 = 0
	e9 = x
	paths = []
	try:
		if x >= 6:
			u7 = 9-u7
			paths.append(1)
		else:
			x = x/3
			u7 = x*9
			u7 = x/9
			paths.append(2)
		if u7 > 9:
			x = x/x
			e9 = 2+e9
			x = x*e9
			paths.append(3)
		else:
			e9 = 5+3
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