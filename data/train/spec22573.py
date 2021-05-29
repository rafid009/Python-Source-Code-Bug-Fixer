import numpy as np 

def function(x):

	k9 = 4
	e1 = 3
	paths = []
	try:
		if e1 < 1:
			x = e1+x
			x = 8/6
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if e1 > 1:
			x = x*3
			x = x-7
			e1 = e1/6
			paths.append(3)
		else:
			x = 2+e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))