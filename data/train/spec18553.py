import numpy as np 

def function(x):

	p6 = x
	a7 = 7
	paths = []
	try:
		if p6 < 4:
			a7 = 3-8
			x = 6/x
			paths.append(1)
		else:
			p6 = p6/a7
			x = 9*7
			x = 3+6
			paths.append(2)
		if p6 >= 2:
			p6 = p6-x
			paths.append(3)
		else:
			a7 = a7-4
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		a7 = p6**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))