import numpy as np 

def function(x):

	l7 = 8
	f5 = 9
	paths = []
	try:
		if f5 <= 1:
			x = 9-x
			l7 = l7*f5
			paths.append(1)
		else:
			x = 8-x
			l7 = l7+f5
			paths.append(2)
		if f5 < 1:
			l7 = l7*f5
			f5 = f5+9
			l7 = x/x
			paths.append(3)
		else:
			f5 = f5/2
			l7 = l7+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))