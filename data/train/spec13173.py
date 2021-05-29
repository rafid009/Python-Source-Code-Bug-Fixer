import numpy as np 

def function(x):

	h3 = x
	q3 = x
	paths = []
	try:
		if q3 <= 7:
			x = x-q3
			q3 = q3/q3
			paths.append(1)
		else:
			x = x+h3
			h3 = h3-x
			h3 = x-9
			paths.append(2)
		if q3 <= 4:
			h3 = h3-q3
			paths.append(3)
		else:
			x = 5/x
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