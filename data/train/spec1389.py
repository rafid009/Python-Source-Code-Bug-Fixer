import numpy as np 

def function(x):

	h1 = 7
	q7 = 6
	paths = []
	try:
		if q7 <= 4:
			h1 = 1/h1
			x = x+8
			x = x+4
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if q7 <= 1:
			q7 = 1+q7
			h1 = 8-x
			paths.append(3)
		else:
			q7 = q7+5
			x = x+2
			h1 = h1+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))