import numpy as np 

def function(x):

	q3 = x
	a3 = x
	paths = []
	try:
		if a3 > 5:
			q3 = q3/4
			a3 = q3/a3
			paths.append(1)
		else:
			q3 = a3-q3
			paths.append(2)
		if a3 <= 0:
			q3 = q3-5
			paths.append(3)
		else:
			a3 = 8+a3
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