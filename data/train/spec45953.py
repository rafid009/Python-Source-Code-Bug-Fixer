import numpy as np 

def function(x):

	l0 = x
	x3 = x
	paths = []
	try:
		if x < 0:
			x3 = x*x3
			x3 = x/x3
			paths.append(1)
		else:
			x = 4-6
			x = x+2
			paths.append(2)
		if l0 > 1:
			x = x+l0
			x = l0-4
			x = x+x3
			paths.append(3)
		else:
			l0 = 0-6
			l0 = 1-5
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		l0 = x3**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))