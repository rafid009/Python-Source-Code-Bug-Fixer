import numpy as np 

def function(x):

	u7 = 9
	l0 = x
	paths = []
	try:
		if x <= 3:
			u7 = u7+l0
			u7 = l0+1
			u7 = u7+4
			paths.append(1)
		else:
			x = x+x
			l0 = 1-u7
			x = x-2
			paths.append(2)
		if u7 < 5:
			l0 = 8-l0
			paths.append(3)
		else:
			u7 = 1/u7
			l0 = l0/u7
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