import numpy as np 

def function(x):

	f2 = 9
	q7 = 4
	paths = []
	try:
		if f2 < 0:
			f2 = 5*f2
			paths.append(1)
		else:
			f2 = q7-f2
			q7 = q7*f2
			paths.append(2)
		if f2 >= 0:
			q7 = 3/q7
			x = 4*x
			q7 = q7+5
			paths.append(3)
		else:
			x = 6-q7
			x = 1-2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		q7 = f2**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))