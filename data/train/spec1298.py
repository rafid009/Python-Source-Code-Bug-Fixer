import numpy as np 

def function(x):

	l0 = x
	h6 = 6
	paths = []
	try:
		if l0 >= 4:
			h6 = 0-9
			paths.append(1)
		else:
			l0 = h6/4
			paths.append(2)
		if l0 > 5:
			x = 9*6
			l0 = 9/x
			l0 = 5-6
			paths.append(3)
		else:
			l0 = x+l0
			x = x+x
			l0 = l0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))