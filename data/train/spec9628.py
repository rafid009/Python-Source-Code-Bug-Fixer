import numpy as np 

def function(x):

	j7 = x
	e7 = x
	paths = []
	try:
		if e7 >= 3:
			e7 = x+x
			paths.append(1)
		else:
			e7 = 3*e7
			e7 = 2+x
			e7 = e7-1
			paths.append(2)
		if j7 <= 6:
			e7 = 3-e7
			j7 = 2/e7
			j7 = j7-1
			paths.append(3)
		else:
			e7 = j7*8
			e7 = 9*e7
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