import numpy as np 

def function(x):

	q9 = 2
	a7 = x
	paths = []
	try:
		if a7 >= 0:
			q9 = a7/9
			q9 = q9*8
			paths.append(1)
		else:
			a7 = 4+4
			a7 = 3/q9
			q9 = a7*q9
			paths.append(2)
		if x >= 6:
			a7 = 0+7
			q9 = q9-0
			x = x/x
			paths.append(3)
		else:
			a7 = x-8
			q9 = a7-q9
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))