import numpy as np 

def function(x):

	q8 = 1
	a5 = x
	paths = []
	try:
		if x >= 2:
			a5 = a5*x
			a5 = a5*x
			paths.append(1)
		else:
			q8 = 0*6
			x = q8+a5
			paths.append(2)
		if q8 < 7:
			q8 = 3+9
			x = 2/4
			q8 = 6*x
			paths.append(3)
		else:
			x = 4*x
			x = x+4
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))