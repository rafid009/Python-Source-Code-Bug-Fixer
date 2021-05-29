import numpy as np 

def function(x):

	q0 = 5
	f2 = x
	paths = []
	try:
		if x > 5:
			f2 = 7*q0
			x = 6*x
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x > 6:
			q0 = q0*f2
			paths.append(3)
		else:
			f2 = x+7
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))