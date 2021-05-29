import numpy as np 

def function(x):

	q3 = 0
	b7 = x
	paths = []
	try:
		if x < 8:
			b7 = b7*b7
			x = 3*x
			b7 = b7*9
			paths.append(1)
		else:
			b7 = 9-b7
			paths.append(2)
		if q3 > 8:
			x = 3*5
			paths.append(3)
		else:
			x = 5*x
			b7 = 3*b7
			q3 = q3-2
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