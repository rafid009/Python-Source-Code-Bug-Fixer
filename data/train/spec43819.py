import numpy as np 

def function(x):

	q1 = x
	a6 = 8
	paths = []
	try:
		if q1 > 4:
			a6 = x-a6
			x = x*9
			paths.append(1)
		else:
			x = a6+7
			paths.append(2)
		if q1 >= 2:
			x = x/x
			x = x/x
			x = 1/7
			paths.append(3)
		else:
			q1 = q1/3
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