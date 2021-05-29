import numpy as np 

def function(x):

	q3 = x
	a0 = 3
	paths = []
	try:
		if a0 <= 9:
			q3 = q3-7
			paths.append(1)
		else:
			q3 = q3*1
			a0 = a0/4
			paths.append(2)
		if x > 9:
			a0 = a0/7
			paths.append(3)
		else:
			a0 = a0/3
			a0 = a0-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))