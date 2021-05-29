import numpy as np 

def function(x):

	q4 = x
	j1 = x
	paths = []
	try:
		if q4 >= 4:
			q4 = 3/q4
			j1 = 6*j1
			paths.append(1)
		else:
			x = q4/3
			x = j1*4
			j1 = 4-j1
			paths.append(2)
		if q4 >= 1:
			x = x-x
			paths.append(3)
		else:
			x = 0+x
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