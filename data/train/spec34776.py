import numpy as np 

def function(x):

	q5 = x
	y6 = 9
	paths = []
	try:
		if y6 <= 4:
			x = x*9
			y6 = y6/4
			q5 = q5*q5
			paths.append(1)
		else:
			q5 = q5/y6
			paths.append(2)
		if y6 <= 0:
			q5 = q5/4
			x = q5*x
			x = x/5
			paths.append(3)
		else:
			x = x-0
			y6 = y6*6
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