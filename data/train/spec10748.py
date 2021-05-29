import numpy as np 

def function(x):

	e3 = x
	l1 = x
	x = 1
	paths = []
	try:
		if l1 > 6:
			l1 = 0-l1
			l1 = l1/8
			paths.append(1)
		else:
			l1 = e3/l1
			l1 = e3+8
			paths.append(2)
		if x >= 8:
			l1 = l1*3
			paths.append(3)
		else:
			e3 = e3-0
			e3 = 9+e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))