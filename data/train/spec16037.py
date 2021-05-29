import numpy as np 

def function(x):

	g3 = x
	q4 = 7
	x = x
	paths = []
	try:
		if x <= 3:
			q4 = q4-3
			q4 = 1/2
			paths.append(1)
		else:
			x = x+4
			q4 = x+q4
			paths.append(2)
		if q4 >= 4:
			x = q4/g3
			paths.append(3)
		else:
			q4 = q4/g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))