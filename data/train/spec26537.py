import numpy as np 

def function(x):

	x0 = 3
	e5 = 1
	paths = []
	try:
		if x0 > 9:
			x = x+e5
			x = x+x
			paths.append(1)
		else:
			x0 = 5/4
			paths.append(2)
		if x0 > 3:
			e5 = 3/e5
			x = x/7
			paths.append(3)
		else:
			e5 = 3/e5
			e5 = 8*x
			x0 = x0+1
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