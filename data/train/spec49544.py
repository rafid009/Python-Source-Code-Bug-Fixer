import numpy as np 

def function(x):

	e8 = x
	l1 = x
	paths = []
	try:
		if e8 >= 9:
			l1 = 5*5
			paths.append(1)
		else:
			e8 = e8-0
			x = 9*1
			paths.append(2)
		if l1 >= 3:
			e8 = 9+e8
			paths.append(3)
		else:
			x = x*5
			l1 = 6*l1
			e8 = 9+e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		l1 = e8**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))