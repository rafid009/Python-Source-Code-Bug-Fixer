import numpy as np 

def function(x):

	l8 = x
	u6 = 8
	paths = []
	try:
		if l8 > 0:
			u6 = 2/1
			l8 = l8-l8
			paths.append(1)
		else:
			x = x+l8
			u6 = l8+l8
			paths.append(2)
		if u6 < 5:
			u6 = u6*6
			paths.append(3)
		else:
			x = 3/x
			x = x*u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		l8 = u6**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))