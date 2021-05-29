import numpy as np 

def function(x):

	u7 = x
	x9 = x
	paths = []
	try:
		if x <= 1:
			u7 = x+u7
			x9 = x9*u7
			paths.append(1)
		else:
			x9 = x9-9
			paths.append(2)
		if x >= 3:
			x9 = x9/x
			u7 = 9-u7
			paths.append(3)
		else:
			x9 = x9/3
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		u7 = x9**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))