import numpy as np 

def function(x):

	j9 = x
	l8 = x
	paths = []
	try:
		if l8 < 1:
			j9 = 7-j9
			j9 = j9+x
			l8 = l8/7
			paths.append(1)
		else:
			j9 = l8-j9
			paths.append(2)
		if x <= 3:
			l8 = l8/5
			l8 = x/4
			l8 = l8*j9
			paths.append(3)
		else:
			l8 = 6*l8
			x = x+9
			x = 2/x
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