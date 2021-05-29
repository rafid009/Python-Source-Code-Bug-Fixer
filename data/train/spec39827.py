import numpy as np 

def function(x):

	a3 = x
	q3 = 4
	paths = []
	try:
		if q3 < 0:
			q3 = 9+a3
			paths.append(1)
		else:
			x = 4+3
			paths.append(2)
		if x > 5:
			q3 = q3-x
			paths.append(3)
		else:
			a3 = q3-a3
			x = x-a3
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))