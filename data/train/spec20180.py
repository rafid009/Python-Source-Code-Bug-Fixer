import numpy as np 

def function(x):

	f5 = x
	l6 = 4
	paths = []
	try:
		if l6 > 7:
			l6 = 0+l6
			f5 = f5*f5
			paths.append(1)
		else:
			f5 = f5+x
			paths.append(2)
		if x <= 1:
			f5 = f5+4
			paths.append(3)
		else:
			l6 = 7+l6
			f5 = f5/3
			f5 = 3*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))