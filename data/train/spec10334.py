import numpy as np 

def function(x):

	q1 = x
	x0 = x
	paths = []
	try:
		if q1 >= 3:
			x = 0*x
			paths.append(1)
		else:
			x0 = 9-x0
			paths.append(2)
		if x0 > 4:
			x0 = 3*x
			x = x/3
			paths.append(3)
		else:
			q1 = q1*9
			x0 = 1+q1
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))