import numpy as np 

def function(x):

	u6 = 4
	l3 = x
	paths = []
	try:
		if l3 < 9:
			l3 = 0+u6
			x = 1-x
			x = x-4
			paths.append(1)
		else:
			l3 = 6/x
			paths.append(2)
		if u6 > 5:
			u6 = u6+1
			paths.append(3)
		else:
			u6 = u6+u6
			u6 = 5/u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))