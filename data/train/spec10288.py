import numpy as np 

def function(x):

	a9 = 3
	h4 = 4
	paths = []
	try:
		if h4 <= 4:
			x = x*1
			a9 = 5-h4
			a9 = 3-8
			paths.append(1)
		else:
			a9 = 2/a9
			x = 4-h4
			h4 = 1-6
			paths.append(2)
		if a9 < 3:
			h4 = 5+h4
			x = a9+1
			x = x-5
			paths.append(3)
		else:
			x = x-9
			h4 = 1-a9
			h4 = 7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))