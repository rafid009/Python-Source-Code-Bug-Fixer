import numpy as np 

def function(x):

	q9 = x
	t7 = x
	paths = []
	try:
		if x <= 4:
			q9 = 1-q9
			paths.append(1)
		else:
			q9 = 5+t7
			paths.append(2)
		if t7 < 6:
			q9 = q9/t7
			x = q9-5
			q9 = 9/q9
			paths.append(3)
		else:
			q9 = 4-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))