import numpy as np 

def function(x):

	h1 = 2
	l1 = 2
	paths = []
	try:
		if h1 >= 9:
			l1 = l1*7
			x = x*3
			x = 9-x
			paths.append(1)
		else:
			x = x-2
			x = 8-x
			paths.append(2)
		if h1 <= 0:
			l1 = 6-x
			h1 = l1*h1
			x = 2+x
			paths.append(3)
		else:
			x = h1*h1
			h1 = h1-7
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		l1 = h1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))