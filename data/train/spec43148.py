import numpy as np 

def function(x):

	l8 = x
	q5 = x
	paths = []
	try:
		if q5 <= 4:
			x = 4*q5
			paths.append(1)
		else:
			q5 = 7/1
			x = x+0
			paths.append(2)
		if q5 <= 5:
			q5 = q5*2
			x = 6/x
			x = x-q5
			paths.append(3)
		else:
			q5 = q5*q5
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