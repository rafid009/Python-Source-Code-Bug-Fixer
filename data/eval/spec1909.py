import numpy as np 

def function(x):

	q9 = 8
	e6 = x
	paths = []
	try:
		if q9 < 8:
			q9 = 2+1
			paths.append(1)
		else:
			q9 = q9-x
			q9 = q9-7
			paths.append(2)
		if x < 6:
			x = e6/x
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))