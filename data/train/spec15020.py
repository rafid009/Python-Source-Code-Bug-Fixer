import numpy as np 

def function(x):

	q4 = 5
	y4 = 1
	paths = []
	try:
		if q4 < 1:
			q4 = 5*7
			y4 = x+1
			paths.append(1)
		else:
			y4 = 1-y4
			y4 = 1*q4
			q4 = y4+0
			paths.append(2)
		if y4 <= 3:
			q4 = q4*x
			x = x+q4
			y4 = y4*q4
			paths.append(3)
		else:
			x = x-q4
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