import numpy as np 

def function(x):

	l1 = 1
	a1 = x
	x = x
	paths = []
	try:
		if x >= 8:
			x = l1*0
			x = x-a1
			a1 = 0-a1
			paths.append(1)
		else:
			l1 = 7+4
			l1 = a1-9
			paths.append(2)
		if x >= 1:
			a1 = 7-4
			paths.append(3)
		else:
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))