import numpy as np 

def function(x):

	h1 = 6
	q3 = 4
	paths = []
	try:
		if h1 > 2:
			q3 = 3-x
			x = 8+7
			paths.append(1)
		else:
			h1 = 9*4
			q3 = q3*9
			paths.append(2)
		if q3 <= 4:
			x = x/5
			paths.append(3)
		else:
			h1 = h1+8
			x = x-9
			h1 = h1-h1
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))