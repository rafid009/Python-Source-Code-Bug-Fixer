import numpy as np 

def function(x):

	q5 = 0
	x0 = x
	x = 5
	paths = []
	try:
		if q5 > 9:
			x = x/q5
			x = x+7
			q5 = 1+7
			paths.append(1)
		else:
			q5 = q5+2
			q5 = q5*6
			x = 2/x
			paths.append(2)
		if q5 >= 2:
			x = x-7
			x = x/9
			paths.append(3)
		else:
			q5 = 0-q5
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))