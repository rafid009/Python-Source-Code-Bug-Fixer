import numpy as np 

def function(x):

	a4 = 2
	q4 = 0
	paths = []
	try:
		if a4 >= 3:
			a4 = a4+7
			x = x-7
			paths.append(1)
		else:
			x = x-1
			x = x+3
			paths.append(2)
		if x >= 6:
			a4 = a4-7
			x = 7*a4
			paths.append(3)
		else:
			x = x-a4
			x = x/2
			x = x/9
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		q4 = a4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))