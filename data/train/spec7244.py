import numpy as np 

def function(x):

	u7 = x
	a2 = x
	paths = []
	try:
		if u7 > 8:
			u7 = u7/3
			a2 = a2-u7
			a2 = 8*a2
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if a2 >= 5:
			x = 6/3
			paths.append(3)
		else:
			x = 0-2
			u7 = u7-4
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))