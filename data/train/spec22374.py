import numpy as np 

def function(x):

	h1 = x
	l6 = 6
	paths = []
	try:
		if h1 > 1:
			h1 = h1-h1
			paths.append(1)
		else:
			h1 = x*0
			l6 = 9-l6
			paths.append(2)
		if h1 >= 7:
			h1 = 3*l6
			x = x-5
			paths.append(3)
		else:
			x = x+x
			h1 = 6+6
			l6 = l6/h1
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