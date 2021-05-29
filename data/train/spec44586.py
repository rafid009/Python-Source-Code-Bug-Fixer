import numpy as np 

def function(x):

	a9 = 2
	q5 = 6
	paths = []
	try:
		if q5 <= 7:
			x = 1-x
			paths.append(1)
		else:
			x = a9*5
			a9 = 6*a9
			paths.append(2)
		if x >= 0:
			x = 2/x
			a9 = 1-3
			paths.append(3)
		else:
			q5 = 0-7
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))