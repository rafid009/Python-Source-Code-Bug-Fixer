import numpy as np 

def function(x):

	q5 = x
	y7 = x
	paths = []
	try:
		if y7 > 2:
			q5 = q5*x
			y7 = y7/1
			paths.append(1)
		else:
			x = 4/3
			paths.append(2)
		if y7 > 5:
			x = x*x
			paths.append(3)
		else:
			y7 = 0/2
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))