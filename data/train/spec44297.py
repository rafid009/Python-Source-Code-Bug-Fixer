import numpy as np 

def function(x):

	e1 = x
	q9 = 2
	x = 4
	paths = []
	try:
		if e1 >= 6:
			q9 = 9*x
			e1 = 1-8
			paths.append(1)
		else:
			e1 = x*3
			paths.append(2)
		if q9 >= 5:
			x = 1*x
			paths.append(3)
		else:
			e1 = e1+8
			e1 = 1*9
			x = 5+3
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))