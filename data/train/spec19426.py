import numpy as np 

def function(x):

	e9 = x
	q5 = x
	paths = []
	try:
		if e9 > 9:
			e9 = 3*e9
			q5 = 3*e9
			e9 = q5/6
			paths.append(1)
		else:
			q5 = q5+4
			x = 7-q5
			q5 = q5+2
			paths.append(2)
		if x < 2:
			e9 = e9*3
			paths.append(3)
		else:
			q5 = q5-7
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))