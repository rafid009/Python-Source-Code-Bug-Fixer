import numpy as np 

def function(x):

	a9 = 3
	h4 = x
	paths = []
	try:
		if x > 3:
			x = 2-a9
			x = 9*4
			paths.append(1)
		else:
			x = a9+0
			x = 4-x
			x = 5*h4
			paths.append(2)
		if h4 < 2:
			h4 = h4/1
			a9 = 7*x
			paths.append(3)
		else:
			h4 = h4+a9
			h4 = h4+0
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))