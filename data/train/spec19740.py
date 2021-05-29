import numpy as np 

def function(x):

	l9 = x
	u1 = 8
	paths = []
	try:
		if u1 <= 1:
			x = x+2
			x = x-2
			u1 = u1-0
			paths.append(1)
		else:
			u1 = u1*l9
			paths.append(2)
		if u1 > 6:
			x = 6/x
			l9 = 7-l9
			paths.append(3)
		else:
			u1 = x-l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))