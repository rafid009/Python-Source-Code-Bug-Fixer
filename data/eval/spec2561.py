import numpy as np 

def function(x):

	x4 = 2
	e2 = x
	paths = []
	try:
		if e2 >= 7:
			x = x/4
			x = x-x4
			paths.append(1)
		else:
			x4 = 0-e2
			x4 = x4/1
			x = x/5
			paths.append(2)
		if x <= 5:
			x4 = 5*x4
			x = x+x
			e2 = e2+4
			paths.append(3)
		else:
			x4 = x4+5
			x = x/x
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		e2 = x4**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))