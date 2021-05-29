import numpy as np 

def function(x):

	o3 = x
	q3 = 3
	paths = []
	try:
		if x > 0:
			q3 = q3+9
			paths.append(1)
		else:
			q3 = q3+3
			q3 = 0-q3
			paths.append(2)
		if q3 >= 2:
			o3 = 7-o3
			x = x-1
			x = x-x
			paths.append(3)
		else:
			o3 = q3-q3
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