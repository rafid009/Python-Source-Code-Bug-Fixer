import numpy as np 

def function(x):

	a5 = x
	q7 = x
	paths = []
	try:
		if q7 < 5:
			q7 = a5-6
			x = x+4
			paths.append(1)
		else:
			q7 = 4*q7
			paths.append(2)
		if a5 <= 3:
			a5 = a5*0
			q7 = 0-q7
			paths.append(3)
		else:
			x = 8-6
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))