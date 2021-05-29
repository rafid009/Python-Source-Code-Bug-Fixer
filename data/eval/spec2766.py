import numpy as np 

def function(x):

	i1 = 6
	u7 = 0
	paths = []
	try:
		if i1 <= 5:
			u7 = i1-x
			paths.append(1)
		else:
			u7 = 9*9
			paths.append(2)
		if x <= 7:
			u7 = 7+u7
			paths.append(3)
		else:
			x = 9-4
			u7 = u7*2
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