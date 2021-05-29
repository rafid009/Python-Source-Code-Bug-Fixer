import numpy as np 

def function(x):

	a5 = 0
	h3 = x
	x = 4
	paths = []
	try:
		if a5 > 1:
			h3 = h3+1
			x = x*5
			paths.append(1)
		else:
			a5 = 7-h3
			a5 = 4+a5
			paths.append(2)
		if x < 1:
			x = x+8
			h3 = h3+4
			paths.append(3)
		else:
			h3 = a5+3
			a5 = h3*5
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))