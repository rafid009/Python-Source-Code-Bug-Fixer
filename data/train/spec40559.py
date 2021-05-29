import numpy as np 

def function(x):

	q3 = x
	c4 = 5
	paths = []
	try:
		if q3 >= 6:
			x = c4-3
			q3 = q3-9
			paths.append(1)
		else:
			x = 8-8
			x = 0/3
			paths.append(2)
		if c4 < 9:
			x = 6+c4
			x = 3*x
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))