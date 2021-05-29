import numpy as np 

def function(x):

	e7 = x
	j3 = 4
	paths = []
	try:
		if x < 8:
			e7 = e7*6
			paths.append(1)
		else:
			j3 = e7*e7
			paths.append(2)
		if x >= 2:
			x = 6-4
			paths.append(3)
		else:
			j3 = e7-2
			j3 = j3-x
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))