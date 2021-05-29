import numpy as np 

def function(x):

	q2 = x
	h1 = 6
	paths = []
	try:
		if x <= 5:
			h1 = h1*9
			x = x/6
			h1 = 8-2
			paths.append(1)
		else:
			h1 = 8/x
			paths.append(2)
		if h1 <= 4:
			h1 = h1-4
			q2 = 9+7
			x = x*6
			paths.append(3)
		else:
			x = 2*x
			h1 = h1-2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))