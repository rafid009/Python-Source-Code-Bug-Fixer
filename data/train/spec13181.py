import numpy as np 

def function(x):

	q2 = 5
	t4 = x
	x = 6
	paths = []
	try:
		if q2 < 8:
			x = x/t4
			q2 = 9-7
			paths.append(1)
		else:
			x = x*t4
			paths.append(2)
		if t4 > 9:
			q2 = q2-t4
			paths.append(3)
		else:
			q2 = q2*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))