import numpy as np 

def function(x):

	e7 = 6
	n1 = 4
	paths = []
	try:
		if n1 > 3:
			n1 = 2-n1
			e7 = 7-n1
			paths.append(1)
		else:
			e7 = 1-e7
			n1 = n1-9
			paths.append(2)
		if x < 4:
			n1 = 6+n1
			x = n1-0
			paths.append(3)
		else:
			x = x+8
			e7 = x+e7
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		e7 = n1**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))