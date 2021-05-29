import numpy as np 

def function(x):

	a1 = x
	q1 = 6
	paths = []
	try:
		if q1 > 7:
			q1 = 1/a1
			q1 = 7+3
			paths.append(1)
		else:
			a1 = a1/5
			a1 = a1*0
			paths.append(2)
		if x > 6:
			q1 = 1/2
			x = x-7
			paths.append(3)
		else:
			x = 8*q1
			x = 1/x
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))