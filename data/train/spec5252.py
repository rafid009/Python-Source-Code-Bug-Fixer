import numpy as np 

def function(x):

	e5 = x
	n3 = x
	paths = []
	try:
		if n3 >= 6:
			e5 = e5-8
			paths.append(1)
		else:
			e5 = e5-x
			paths.append(2)
		if n3 >= 3:
			x = n3+8
			x = 7*x
			paths.append(3)
		else:
			x = x/x
			n3 = n3+3
			e5 = e5-5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))