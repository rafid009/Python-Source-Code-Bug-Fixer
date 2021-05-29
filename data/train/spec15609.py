import numpy as np 

def function(x):

	q0 = x
	f1 = 4
	paths = []
	try:
		if x < 3:
			x = x-6
			f1 = 3-f1
			paths.append(1)
		else:
			x = f1*x
			f1 = q0*5
			f1 = f1+7
			paths.append(2)
		if q0 < 8:
			x = 9/x
			q0 = 3-q0
			paths.append(3)
		else:
			q0 = 6-q0
			f1 = 2-3
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))