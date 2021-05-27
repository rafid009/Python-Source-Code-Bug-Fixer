import numpy as np 

def function(x):

	u7 = x
	l0 = 3
	paths = []
	try:
		if u7 <= 4:
			u7 = u7-8
			paths.append(1)
		else:
			l0 = l0-8
			paths.append(2)
		if l0 > 1:
			x = 8/x
			x = 8*l0
			u7 = u7/1
			paths.append(3)
		else:
			x = x+3
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