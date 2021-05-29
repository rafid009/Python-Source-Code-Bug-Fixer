import numpy as np 

def function(x):

	u7 = x
	l6 = 5
	paths = []
	try:
		if u7 >= 7:
			u7 = 4/u7
			u7 = l6*7
			u7 = u7-3
			paths.append(1)
		else:
			x = 8/x
			paths.append(2)
		if l6 > 9:
			l6 = l6-7
			x = 5+2
			x = l6+x
			paths.append(3)
		else:
			u7 = 8*u7
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