import numpy as np 

def function(x):

	q7 = 5
	i8 = 6
	paths = []
	try:
		if q7 >= 3:
			q7 = 3/i8
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if i8 < 4:
			i8 = i8/q7
			paths.append(3)
		else:
			i8 = 4-i8
			q7 = q7+x
			q7 = q7-4
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))