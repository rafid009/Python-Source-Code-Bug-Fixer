import numpy as np 

def function(x):

	a0 = x
	h1 = x
	paths = []
	try:
		if h1 <= 3:
			x = 9/x
			a0 = a0+h1
			a0 = a0+a0
			paths.append(1)
		else:
			x = 1+x
			h1 = h1+h1
			h1 = 5+9
			paths.append(2)
		if a0 <= 8:
			x = x+7
			h1 = a0+h1
			h1 = h1-0
			paths.append(3)
		else:
			a0 = 7-a0
			h1 = h1+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))