import numpy as np 

def function(x):

	a1 = 4
	h1 = 9
	paths = []
	try:
		if a1 >= 4:
			h1 = h1*a1
			x = 0-3
			paths.append(1)
		else:
			a1 = x-3
			x = x+a1
			x = 7-2
			paths.append(2)
		if h1 <= 6:
			x = 3*8
			h1 = h1*8
			paths.append(3)
		else:
			h1 = 2+a1
			a1 = 9*x
			x = 7+a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))