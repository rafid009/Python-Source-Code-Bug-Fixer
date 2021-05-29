import numpy as np 

def function(x):

	u2 = x
	l8 = x
	paths = []
	try:
		if l8 <= 3:
			l8 = 5*u2
			x = x-u2
			x = x-1
			paths.append(1)
		else:
			u2 = u2/1
			l8 = l8/7
			paths.append(2)
		if u2 <= 1:
			x = x*l8
			x = 7/x
			paths.append(3)
		else:
			u2 = u2+u2
			u2 = 5-u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		l8 = u2**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))