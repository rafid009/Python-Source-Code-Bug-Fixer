import numpy as np 

def function(x):

	f7 = 5
	l7 = x
	paths = []
	try:
		if l7 < 4:
			x = x+8
			paths.append(1)
		else:
			l7 = 9-l7
			l7 = l7/4
			f7 = f7+l7
			paths.append(2)
		if x > 3:
			f7 = f7+l7
			x = 0-x
			l7 = x/l7
			paths.append(3)
		else:
			f7 = f7*f7
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