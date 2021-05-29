import numpy as np 

def function(x):

	a2 = 7
	e2 = x
	paths = []
	try:
		if e2 > 0:
			e2 = e2*1
			paths.append(1)
		else:
			e2 = 8-3
			a2 = 7*9
			paths.append(2)
		if e2 >= 8:
			a2 = a2/9
			x = 0/a2
			e2 = 6-1
			paths.append(3)
		else:
			x = x+8
			a2 = a2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))