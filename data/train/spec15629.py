import numpy as np 

def function(x):

	l9 = 7
	u4 = x
	paths = []
	try:
		if x < 1:
			u4 = 9-l9
			paths.append(1)
		else:
			x = 0+2
			l9 = l9-9
			l9 = x-l9
			paths.append(2)
		if l9 > 6:
			l9 = 0-l9
			l9 = l9+u4
			u4 = l9/l9
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))