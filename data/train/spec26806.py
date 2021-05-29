import numpy as np 

def function(x):

	q7 = 1
	a6 = x
	paths = []
	try:
		if a6 <= 7:
			a6 = 3-x
			a6 = 5*a6
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if a6 >= 7:
			q7 = x+q7
			paths.append(3)
		else:
			a6 = a6/q7
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		q7 = a6**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))