import numpy as np 

def function(x):

	l1 = 7
	e3 = x
	paths = []
	try:
		if x < 5:
			e3 = 7/4
			paths.append(1)
		else:
			x = 4*x
			e3 = 2-e3
			x = x-x
			paths.append(2)
		if x >= 7:
			x = 0/x
			l1 = l1+e3
			x = x+3
			paths.append(3)
		else:
			l1 = 1/9
			e3 = 4*x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))