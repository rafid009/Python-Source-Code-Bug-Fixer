import numpy as np 

def function(x):

	a6 = x
	q5 = x
	paths = []
	try:
		if x >= 6:
			x = x/x
			q5 = q5+7
			paths.append(1)
		else:
			a6 = 2*q5
			x = x-8
			paths.append(2)
		if q5 >= 4:
			q5 = 5*5
			paths.append(3)
		else:
			x = x/a6
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))