import numpy as np 

def function(x):

	h3 = x
	l0 = 0
	paths = []
	try:
		if h3 > 2:
			h3 = h3+2
			h3 = x/6
			x = 1*x
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if x <= 5:
			x = x-l0
			paths.append(3)
		else:
			h3 = 8+l0
			h3 = 1*7
			h3 = h3+h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		l0 = h3**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))