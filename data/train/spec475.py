import numpy as np 

def function(x):

	x0 = x
	q9 = 2
	paths = []
	try:
		if x0 > 7:
			q9 = q9-8
			paths.append(1)
		else:
			q9 = 5-q9
			q9 = x*0
			paths.append(2)
		if x < 3:
			x = x/x
			q9 = q9*x
			q9 = 6*x0
			paths.append(3)
		else:
			x = q9-x
			x = x-x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))