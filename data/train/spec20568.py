import numpy as np 

def function(x):

	l5 = 4
	h2 = x
	paths = []
	try:
		if h2 > 0:
			l5 = 6-l5
			l5 = h2/h2
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if h2 >= 8:
			h2 = 1-6
			paths.append(3)
		else:
			x = 1+6
			x = x+h2
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		l5 = h2**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))