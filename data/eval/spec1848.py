import numpy as np 

def function(x):

	h2 = x
	l0 = x
	x = 5
	paths = []
	try:
		if h2 <= 6:
			l0 = l0-l0
			paths.append(1)
		else:
			h2 = 7/9
			x = 9-h2
			l0 = 9+l0
			paths.append(2)
		if x > 9:
			x = 3/h2
			paths.append(3)
		else:
			h2 = l0+h2
			x = 7*x
			l0 = l0+l0
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))