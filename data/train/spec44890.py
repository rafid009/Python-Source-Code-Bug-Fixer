import numpy as np 

def function(x):

	f4 = 1
	l4 = x
	paths = []
	try:
		if x > 7:
			x = f4+l4
			x = 7/3
			paths.append(1)
		else:
			f4 = 3+f4
			l4 = l4*9
			l4 = 0/7
			paths.append(2)
		if l4 < 7:
			l4 = 9-x
			x = l4/x
			x = x-3
			paths.append(3)
		else:
			l4 = 3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))