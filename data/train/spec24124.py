import numpy as np 

def function(x):

	a7 = x
	q0 = x
	paths = []
	try:
		if q0 <= 8:
			x = x*9
			a7 = x*q0
			q0 = q0/8
			paths.append(1)
		else:
			a7 = 5+6
			a7 = x*a7
			q0 = 6*q0
			paths.append(2)
		if x > 5:
			a7 = x-a7
			paths.append(3)
		else:
			q0 = 3-7
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))