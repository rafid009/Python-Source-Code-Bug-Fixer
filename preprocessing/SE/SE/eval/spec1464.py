import numpy as np 

def function(x):

	l3 = x
	h1 = 5
	x = 7
	paths = []
	try:
		if x <= 7:
			l3 = 1*l3
			h1 = h1*6
			x = x-h1
			paths.append(1)
		else:
			h1 = 3*1
			paths.append(2)
		if h1 > 7:
			x = x/l3
			l3 = 0-6
			paths.append(3)
		else:
			x = 9-x
			h1 = h1-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))