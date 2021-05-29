import numpy as np 

def function(x):

	l8 = x
	u6 = x
	paths = []
	try:
		if l8 >= 8:
			l8 = l8+0
			x = x-3
			paths.append(1)
		else:
			u6 = u6-0
			u6 = u6+u6
			u6 = 1-u6
			paths.append(2)
		if u6 >= 2:
			x = x/4
			paths.append(3)
		else:
			l8 = x-6
			l8 = l8+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))